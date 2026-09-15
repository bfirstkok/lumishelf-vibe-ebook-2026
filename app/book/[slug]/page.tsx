import Image from "next/image";
import Link from "next/link";
import { ArrowLeft, CheckCircle2, Clock3, Download, FileText } from "lucide-react";
import { notFound } from "next/navigation";
import { books, formatBaht, getBook } from "@/lib/books";

export function generateStaticParams() { return books.map((book) => ({ slug: book.slug })); }

export default async function BookPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const book = getBook(slug);
  if (!book) notFound();
  return <section className="detail-page"><Link className="back-link" href="/"><ArrowLeft size={17} /> กลับไปชั้นหนังสือ</Link><div className="detail-grid"><div className="detail-cover"><div className="cover-glow" style={{ background: book.accent }} /><Image src={book.cover} alt={`ปก ${book.title}`} width={420} height={580} priority /></div><div className="detail-copy"><span className="category">{book.category}</span><h1>{book.title}</h1><p className="subtitle">{book.subtitle}</p><p className="description">{book.description}</p><div className="detail-facts"><span><FileText /> PDF · {book.pages} หน้า</span><span><Clock3 /> อ่านประมาณ {Math.max(2, book.pages * 2)} นาที</span><span><Download /> ดาวน์โหลดหลังชำระ</span></div><div className="purchase-box"><div><small>ราคา E-book</small><strong>{formatBaht(book.price)}</strong></div><Link className="primary-button wide" href={`/checkout/${book.slug}`}>เลือกเล่มนี้</Link></div><p className="fine-print"><CheckCircle2 size={16} /> ดาวน์โหลด PDF หลังชำระเงินจำลอง · ระบบสาธิต ไม่มีการรับเงินจริง</p></div></div></section>;
}
