import {NextResponse} from 'next/server';
import {authorizedOrder,noCache,serializeOrder} from '@/lib/order-server';
export async function GET(_request:Request,{params}:{params:Promise<{id:string}>}){
 try{const data=await authorizedOrder((await params).id);if(!data)return NextResponse.json({error:'ไม่พบคำสั่งซื้อหรือสิทธิ์หมดอายุ กรุณาค้นหาด้วยหมายเลขและอีเมล'},{status:404,headers:noCache});return NextResponse.json(await serializeOrder(data),{headers:noCache});}
 catch{return NextResponse.json({error:'โหลดคำสั่งซื้อไม่ได้ กรุณาลองใหม่'},{status:503,headers:noCache});}
}
