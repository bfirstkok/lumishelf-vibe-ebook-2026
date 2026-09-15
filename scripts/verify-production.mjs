import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
const base='https://vibecode-gamma-murex.vercel.app', checks=[];let cookie='';
async function req(path,body,auth=true){const r=await fetch(base+path,{method:body?'POST':'GET',headers:{...(body?{'Content-Type':'application/json',Origin:base}:{}),...(auth&&cookie?{Cookie:cookie}:{})},body:body?JSON.stringify(body):undefined});const set=r.headers.get('set-cookie');if(auth&&set)cookie=set.split(';')[0];return [r,await r.json()];}
function ok(name,value){assert.ok(value,name);checks.push({name,passed:true});console.log('PASS',name);}
let [r,d]=await req('/api/orders',{bookId:'bad'});ok('Invalid checkout rejected',r.status===400);
[r,d]=await req('/api/orders',{bookId:'media-player-pro',customerName:'Production QA',customerEmail:'demo@example.com',total:1});ok('Creates real PENDING order with server price',r.status===201&&d.status==='PENDING'&&d.total===199&&!d.downloadUrl);const id=d.id,number=d.orderNumber;
ok('No secret/hash in response',!JSON.stringify(d).match(/sb_secret_|access_token_hash/));
[r]=await req('/api/orders/'+id,undefined,false);ok('Order ID alone cannot read order',r.status===404);
[r]=await req('/api/orders/lookup',{orderNumber:number,email:'wrong@example.com'});ok('Wrong email cannot look up order',r.status===404);
[r,d]=await req('/api/orders/'+id+'/pay',{});ok('Mock payment persists PAID and simulated email',r.status===200&&d.status==='PAID'&&d.emailStatus==='SIMULATED'&&!!d.downloadUrl);
const download=await fetch(d.downloadUrl);ok('Signed URL downloads actual PDF',download.ok&&Buffer.from(await download.arrayBuffer()).subarray(0,4).toString()==='%PDF');
const signed=new URL(d.downloadUrl);const token=signed.searchParams.get('token');const claims=JSON.parse(Buffer.from(token.split('.')[1],'base64url'));ok('Signed link expires in 15 minutes',claims.exp-claims.iat===900);
signed.searchParams.set('token',token.slice(0,-8)+'invalid!');ok('Tampered download token rejected',!(await fetch(signed)).ok);
[r,d]=await req('/api/orders/'+id+'/pay',{});ok('Repeated mock payment is safe',r.status===200&&d.status==='PAID');
cookie='';[r,d]=await req('/api/orders/lookup',{orderNumber:number,email:'demo@example.com'});ok('Correct number and email restore access',r.status===200&&d.id===id);
[r,d]=await req('/api/orders/'+id);ok('Order remains PAID in new session',r.status===200&&d.status==='PAID');
const sb='https://kkyciqcngrcqimfchavk.supabase.co',key='sb_publishable_mh-GNiPPyudUd3XRLtap5g_jQVNWXB5';
ok('Anonymous access to orders rejected',!(await fetch(sb+'/rest/v1/orders?select=id',{headers:{apikey:key}})).ok);
ok('Private PDF cannot be downloaded publicly',!(await fetch(sb+'/storage/v1/object/public/ebooks/media-player-pro.pdf')).ok);
const catalog=await fetch(sb+'/rest/v1/books?select=id',{headers:{apikey:key}});ok('Six books stored in Supabase',(await catalog.json()).length===6);
writeFileSync('docs/production-test-results.json',JSON.stringify({testedAt:new Date().toISOString(),base,orderNumber:number,checks},null,2));
