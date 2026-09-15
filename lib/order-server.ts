import { randomBytes, createHash, timingSafeEqual } from 'node:crypto';
import { cookies } from 'next/headers';
import { getSupabaseAdmin } from './supabase-admin';
import { getBook } from './books';
export const noCache = { 'Cache-Control': 'private, no-store', 'Referrer-Policy': 'no-referrer' };
export const tokenHash = (s: string) => createHash('sha256').update(s).digest('hex');
export const newToken = () => randomBytes(32).toString('hex');
export const newOrderNumber = () => 'LS-'+new Date().toISOString().slice(0,10).replaceAll('-','')+'-'+randomBytes(8).toString('hex').toUpperCase();
export const sameOrigin = (r:Request) => !r.headers.get('origin') || r.headers.get('origin')===new URL(r.url).origin;
export async function grantOrderAccess(id:string,token:string) {
 (await cookies()).set('ls_'+id,token,{httpOnly:true,secure:process.env.NODE_ENV==='production',sameSite:'lax',path:'/',maxAge:86400});
}
export async function authorizedOrder(id:string) {
 if(!/^[a-f0-9-]{36}$/i.test(id))return null;
 const token=(await cookies()).get('ls_'+id)?.value;
 if(!token||!/^[a-f0-9]{64}$/.test(token))return null;
 const {data,error}=await getSupabaseAdmin().from('orders').select('*').eq('id',id).maybeSingle();
 if(error)throw error;
 if(!data||typeof data.access_token_hash!=='string')return null;
 const a=Buffer.from(tokenHash(token),'hex'),b=Buffer.from(data.access_token_hash,'hex');
 return a.length===b.length&&timingSafeEqual(a,b)?data:null;
}
export async function serializeOrder(d:Record<string,unknown>) {
 let downloadUrl:string|undefined;let downloadError:string|undefined;
 if(d.status==='PAID'){
  const book=getBook(String(d.book_id));
  if(book){const {data,error}=await getSupabaseAdmin().storage.from('ebooks').createSignedUrl(book.filePath,900,{download:book.filePath}); if(error||!data)downloadError='ยังสร้างลิงก์ไม่ได้ กรุณารีเฟรชอีกครั้ง';else downloadUrl=data.signedUrl;}
 }
 return {id:d.id,orderNumber:d.order_number,bookId:d.book_id,customerName:d.customer_name,customerEmail:d.customer_email,total:Number(d.total),status:d.status,createdAt:d.created_at,emailStatus:d.email_status,downloadUrl,downloadError};
}
