import {NextResponse} from 'next/server';
import {getSupabaseAdmin} from '@/lib/supabase-admin';
import {authorizedOrder,noCache,sameOrigin,serializeOrder} from '@/lib/order-server';
export async function POST(request:Request,{params}:{params:Promise<{id:string}>}){
 if(!sameOrigin(request))return NextResponse.json({error:'ไม่อนุญาตคำขอ'},{status:403});
 try{
 const existing=await authorizedOrder((await params).id);if(!existing)return NextResponse.json({error:'ไม่พบคำสั่งซื้อหรือไม่มีสิทธิ์'},{status:404,headers:noCache});
 let order=existing;
 if(existing.status==='PENDING'){const {data,error}=await getSupabaseAdmin().from('orders').update({status:'PAID',paid_at:new Date().toISOString()}).eq('id',existing.id).eq('status','PENDING').select().maybeSingle();if(error)throw error;order=data||await authorizedOrder(existing.id);if(!order)throw Error('Missing order');}
 const result=await serializeOrder(order);
 // Visible simulation allowed by worksheet. This does not send real email.
 if(result.downloadUrl&&order.email_status==='NOT_SENT'){const {error}=await getSupabaseAdmin().from('orders').update({email_status:'SIMULATED'}).eq('id',order.id);if(error)throw error;result.emailStatus='SIMULATED';}
 return NextResponse.json(result,{headers:noCache});
 }catch{return NextResponse.json({error:'ดำเนินการไม่สำเร็จ กรุณารีเฟรชตรวจสถานะก่อนลองใหม่'},{status:503,headers:noCache});}
}
