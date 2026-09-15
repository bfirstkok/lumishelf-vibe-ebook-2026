import type { Metadata } from "next";
import Link from "next/link";
import { BookOpenText, Search, Sparkles } from "lucide-react";
import "./globals.css";

export const metadata: Metadata = {
  title: "LumiShelf — E-books for slower days",
  description: "ร้าน E-book ตัวอย่างสำหรับใบงาน Vibe Coding 2026",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="th" data-scroll-behavior="smooth">
      <body>
        <div className="demo-ribbon"><Sparkles size={14} /> DEMO ONLY — ระบบจำลอง ไม่มีการรับเงินจริง</div>
        <header className="site-header">
          <Link className="brand" href="/"><span className="brand-mark"><BookOpenText /></span><span>LumiShelf<small>stories to keep</small></span></Link>
          <nav aria-label="เมนูหลัก"><Link href="/">หนังสือ</Link><Link href="/track"><Search size={17} /> ติดตามคำสั่งซื้อ</Link></nav>
        </header>
        <main>{children}</main>
        <footer><div><strong>LumiShelf</strong><p>หนังสือดิจิทัลสำหรับวันธรรมดาที่อยากพักใจ</p></div><p>โปรเจกต์สาธิตเพื่อการศึกษา · ไม่มีการชำระเงินจริง</p></footer>
      </body>
    </html>
  );
}
