# LumiShelf - Vibe Coding E-book 2026

ร้าน E-book สำหรับลูกค้า สร้างด้วย Next.js, Supabase และ Vercel พร้อม Android WebViewer จาก MIT App Inventor

## Production

- Web: https://vibecode-gamma-murex.vercel.app
- Source: https://github.com/bfirstkok/lumishelf-vibe-ebook-2026
- Catalog: 6 เล่ม รวม Media Player PRO, Tarot App และ SQLite Task Manager PRO

## Flow

เลือกหนังสือ -> กรอกชื่อ/อีเมล -> บันทึก PENDING -> กดชำระเงินจำลอง (DEMO ONLY) -> PAID -> แสดงอีเมลจำลองสำเร็จและ signed URL อายุ 15 นาที

ค้นหาออเดอร์ต้องใช้หมายเลขและอีเมลที่ตรงกัน เซิร์ฟเวอร์ออก HTTP-only cookie เฉพาะออเดอร์ และไม่ส่ง secret key ไปยัง client

## Local setup

1. คัดลอก `.env.example` เป็น `.env.local` และใส่ค่า Supabase
2. รัน `supabase/schema.sql`
3. รัน `npm install` และ `npm run dev`

## Verify

`npm run lint`, `npm run build`, `npm test`, `node scripts/verify-production.mjs`

ไฟล์ PDF ต้นฉบับอยู่ใน `private/ebooks` และถูกกันออกจาก Git/Vercel; production ใช้ Supabase Storage bucket `ebooks` แบบ private เท่านั้น

## Android

`mobile/LumiShelf.aia` เปิดด้วย MIT App Inventor และ `mobile/LumiShelf.apk` ติดตั้งบน Android ได้ WebViewer เปิด production URL, FollowLinks=true, IgnoreSslErrors=false, UsesLocation=false และ Back จะย้อนหน้าเว็บก่อนปิดแอป
