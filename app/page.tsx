import Image from "next/image";
import Link from "next/link";
import { ArrowRight, BookHeart, Download, ShieldCheck } from "lucide-react";
import { books, formatBaht } from "@/lib/books";

export default function Home() {
  return (
    <>
      <section className="hero">
        <div className="hero-copy"><span className="eyebrow">CURATED DIGITAL BOOKS · 2026</span><h1>อ่านช้าลง<br /><em>รู้สึกได้มากขึ้น</em></h1><p>เลือกเรื่องที่ใช่สำหรับคืนนี้ แล้วพกโลกอีกใบติดตัวไปได้ทุกที่</p><a className="primary-button" href="#collection">สำรวจชั้นหนังสือ <ArrowRight size={18} /></a></div>
        <div className="hero-art" aria-hidden="true"><div className="moon" /><Image className="hero-cover cover-back" src={books[2].cover} alt="" width={230} height={320} /><Image className="hero-cover cover-front" src={books[0].cover} alt="" width={250} height={350} /><span className="orbit one">✦</span><span className="orbit two">✧</span></div>
      </section>
      <section className="feature-strip"><div><BookHeart /><span><strong>คัดสรรอย่างตั้งใจ</strong>{books.length} เรื่อง ทั้งอ่านเพลินและลงมือสร้าง</span></div><div><ShieldCheck /><span><strong>สั่งซื้ออย่างปลอดภัย</strong>ไม่เปิดเผยข้อมูลผู้อื่น</span></div><div><Download /><span><strong>พร้อมดาวน์โหลด</strong>เมื่อชำระเงินสำเร็จ</span></div></section>
      <section className="collection" id="collection"><div className="section-heading"><div><span className="eyebrow">THE COLLECTION</span><h2>เลือกเล่มถัดไปของคุณ</h2></div><p>{books.length} เล่มบนชั้น</p></div>
        <div className="book-grid">{books.map((book, index) => <article className="book-card" key={book.id}><Link href={`/book/${book.slug}`} className="cover-wrap"><span className="book-index">0{index + 1}</span><Image src={book.cover} alt={`ปกหนังสือ ${book.title}`} width={360} height={500} priority={index === 0} /></Link><div className="book-info"><span className="category">{book.category}</span><h3><Link href={`/book/${book.slug}`}>{book.title}</Link></h3><p>{book.description}</p><div className="book-meta"><strong>{formatBaht(book.price)}</strong><span>{book.pages} หน้า</span></div><Link className="card-button" href={`/book/${book.slug}`}>ดูรายละเอียด <ArrowRight size={16} /></Link></div></article>)}</div>
      </section>
    </>
  );
}
