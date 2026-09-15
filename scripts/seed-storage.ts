import {createClient} from '@supabase/supabase-js';
import {readFile} from 'node:fs/promises';
import {books} from '../lib/books';
const db=createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!,process.env.SUPABASE_SECRET_KEY!,{auth:{persistSession:false}});
async function main(){
 for(const b of books){
  const {error}=await db.from('books').upsert({id:b.id,slug:b.slug,title:b.title,subtitle:b.subtitle,description:b.description,price:b.price,category:b.category,pages:b.pages,cover_url:b.cover,file_path:b.filePath});
  if(error)throw Error(error.message);
  const {error:upload}=await db.storage.from('ebooks').upload(b.filePath,await readFile('private/ebooks/'+b.filePath),{contentType:'application/pdf',upsert:true});
  if(upload)throw Error(upload.message);console.log('Seeded and uploaded: '+b.slug);
 }
 const {data,error}=await db.from('books').select('slug,pages');if(error)throw Error(error.message);console.log(data);
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
