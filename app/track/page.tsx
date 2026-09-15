"use client";
import Link from 'next/link';
import {Search,ArrowRight} from 'lucide-react';
import {useRouter} from 'next/navigation';
import {useState,FormEvent} from 'react';
export default function TrackPage(){
 const router=useRouter();const [number,setNumber]=useState(''),[email,setEmail]=useState(''),[error,setError]=useState(''),[busy,setBusy]=useState(false);
 async function submit(e:FormEvent){e.preventDefault();setBusy(true);setError('');try{const res=await fetch('/api/orders/lookup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({orderNumber:number,email})});const data=await res.json();if(!res.ok)throw Error(data.error);router.push('/order/'+data.id);}catch(err){setError(err instanceof Error?err.message:'ค้นหาไม่ได้ กรุณาลองใหม่');setBusy(false);}}
 return <section className="track-page"><div className="track-icon"><Search/></div><span className="eyebrow">ORDER TRACKING</span><h1>หนังสือของคุณอยู่ตรงนี้</h1><p>ใช้หมายเลขคำสั่งซื้อและอีเมลเดียวกับตอนสั่งซื้อ ค้นหาได้แม้เปลี่ยนเครื่อง</p><form onSubmit={submit}><label>หมายเลขคำสั่งซื้อ<input value={number} onChange={e=>setNumber(e.target.value)} placeholder="LS-20260914-0123456789ABCDEF" required/></label><label>อีเมลที่ใช้สั่งซื้อ<input type="email" value={email} onChange={e=>setEmail(e.target.value)} required placeholder="name@example.com"/></label>{error&&<p className="form-error" role="alert">{error}</p>}<button className="primary-button wide" disabled={busy}>{busy?'กำลังค้นหา…':<>ค้นหาคำสั่งซื้อ<ArrowRight size={18}/></>}</button></form><Link href="/" className="text-link">กลับไปเลือกหนังสือ</Link></section>;
}
