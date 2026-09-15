"use client";

import Image from "next/image";
import Link from "next/link";
import { ArrowLeft, LockKeyhole, Mail, UserRound } from "lucide-react";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";
import type { Book } from "@/lib/books";
import { formatBaht } from "@/lib/books";
import { isValidEmail } from "@/lib/orders";

export default function CheckoutForm({ book }: { book: Book }) {
  const router = useRouter();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit(event: FormEvent) {
    event.preventDefault(); setError("");
    if (name.trim().length < 2) return setError("กรุณากรอกชื่ออย่างน้อย 2 ตัวอักษร");
    if (!isValidEmail(email)) return setError("กรุณากรอกอีเมลให้ถูกต้อง");
    setLoading(true);
    try {
      const response = await fetch("/api/orders", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ bookId: book.id, customerName: name, customerEmail: email }) });
      const order = await response.json();
      if (!response.ok) throw new Error(order.error || 'สร้างคำสั่งซื้อไม่ได้');
      router.push(`/order/${order.id}`);
    } catch (err) { setError(err instanceof Error ? err.message : 'เชื่อมต่อไม่ได้ กรุณาลองใหม่'); setLoading(false); }
  }

  return <section className="checkout-page"><Link className="back-link" href={`/book/${book.slug}`}><ArrowLeft size={17} /> กลับไปหน้าหนังสือ</Link><div className="checkout-grid"><form className="checkout-form" onSubmit={submit}><span className="step">ขั้นตอนที่ 1 จาก 2</span><h1>ข้อมูลสำหรับรับหนังสือ</h1><p>ใช้อีเมลนี้ติดตามคำสั่งซื้อ โดยระบบจะแสดงตัวอย่างอีเมลจำลอง ไม่ส่งอีเมลจริง</p><label><span><UserRound size={18} /> ชื่อผู้สั่งซื้อ</span><input value={name} onChange={(e) => setName(e.target.value)} placeholder="เช่น ลลิน แสงดาว" autoComplete="name" /></label><label><span><Mail size={18} /> อีเมล</span><input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="name@example.com" type="email" autoComplete="email" /></label>{error && <p className="form-error" role="alert">{error}</p>}<button className="primary-button wide" disabled={loading}>{loading ? "กำลังสร้างคำสั่งซื้อ…" : "ยืนยันคำสั่งซื้อ"}</button><p className="security-note"><LockKeyhole size={15} /> ข้อมูลใช้เฉพาะคำสั่งซื้อนี้เท่านั้น</p></form><aside className="order-summary"><span className="eyebrow">ORDER SUMMARY</span><h2>สรุปคำสั่งซื้อ</h2><div className="summary-book"><Image src={book.cover} alt="" width={92} height={128} /><div><strong>{book.title}</strong><span>{book.category}</span><span>ไฟล์ PDF · {book.pages} หน้า</span></div></div><div className="summary-row"><span>ราคา</span><span>{formatBaht(book.price)}</span></div><div className="summary-row"><span>ค่าจัดส่ง</span><span>ฟรี</span></div><div className="summary-total"><span>ยอดรวม</span><strong>{formatBaht(book.price)}</strong></div><div className="demo-notice"><strong>DEMO ONLY</strong><p>ขั้นตอนถัดไปเป็นการจำลองชำระเงิน ไม่มีการตัดเงินจริง</p></div></aside></div></section>;
}
