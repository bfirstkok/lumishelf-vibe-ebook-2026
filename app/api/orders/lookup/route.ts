import {NextResponse} from 'next/server';
import {getSupabaseAdmin} from '@/lib/supabase-admin';
import {isValidEmail,normalizeEmail} from '@/lib/orders';
import {grantOrderAccess,newToken,noCache,sameOrigin,tokenHash} from '@/lib/order-server';
export async function POST(request:Request){
 if(!sameOrigin(request))return NextResponse.json({error:'ไม่อนุญาตคำขอ'},{status:403});
 try{
 const body=await request.json(),number=typeof body.orderNumber==='string'?body.orderNumber.trim().toUpperCase():'',email=typeof body.email==='string'?normalizeEmail(body.email):'';
 const missing=()=>NextResponse.json({error:'ไม่พบคำสั่งซื้อที่ตรงกับหมายเลขและอีเมลนี้'},{status:404,headers:noCache});
 if(!/^LS-\d{8}-[A-F0-9]{16}$/.test(number)||email.length>254||!isValidEmail(email))return missing();
 const db=getSupabaseAdmin();const {data,error}=await db.from('orders').select('id').eq('order_number',number).eq('customer_email',email).maybeSingle();
 if(error)throw error;if(!data)return missing();
 const token=newToken();const {error:updated}=await db.from('orders').update({access_token_hash:tokenHash(token)}).eq('id',data.id);
 if(updated)throw updated;await grantOrderAccess(data.id,token);return NextResponse.json({id:data.id},{headers:noCache});
 }catch{return NextResponse.json({error:'ค้นหาไม่ได้ชั่วคราว กรุณาลองใหม่'},{status:503,headers:noCache});}
}
