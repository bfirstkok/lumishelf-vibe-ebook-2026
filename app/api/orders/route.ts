import {NextResponse} from 'next/server';
import {getBook} from '@/lib/books';
import {isValidEmail,normalizeEmail} from '@/lib/orders';
import {getSupabaseAdmin} from '@/lib/supabase-admin';
import {grantOrderAccess,newOrderNumber,newToken,noCache,sameOrigin,serializeOrder,tokenHash} from '@/lib/order-server';
export async function POST(request:Request){
 if(!sameOrigin(request))return NextResponse.json({error:'ไม่อนุญาตคำขอจากเว็บไซต์อื่น'},{status:403});
 try{
 const body=await request.json(),book=getBook(typeof body.bookId==='string'?body.bookId:'');
 const name=typeof body.customerName==='string'?body.customerName.trim():'';
 const email=typeof body.customerEmail==='string'?normalizeEmail(body.customerEmail):'';
 if(!book||name.length<2||name.length>100||email.length>254||!isValidEmail(email))return NextResponse.json({error:'กรุณาตรวจชื่อ อีเมล และหนังสือที่เลือก'},{status:400});
 const token=newToken();
 const {data,error}=await getSupabaseAdmin().from('orders').insert({order_number:newOrderNumber(),book_id:book.id,customer_name:name,customer_email:email,total:book.price,status:'PENDING',access_token_hash:tokenHash(token)}).select().single();
 if(error)throw error;await grantOrderAccess(data.id,token);
 return NextResponse.json(await serializeOrder(data),{status:201,headers:noCache});
 }catch(error){return NextResponse.json({error:'บันทึกคำสั่งซื้อไม่ได้ กรุณาลองใหม่'},{status:error instanceof SyntaxError?400:503,headers:noCache});}
}
