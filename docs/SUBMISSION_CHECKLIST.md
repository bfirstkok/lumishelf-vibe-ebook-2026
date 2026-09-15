# ตรวจครบตามใบงาน Vibe Coding E-book 2026

- [x] ร้าน E-book สำหรับลูกค้า ไม่มีหน้าผู้ดูแล
- [x] หนังสือ 6 เล่ม รวม Media Player PRO, Tarot App, SQLite Task Manager PRO
- [x] ปก ชื่อ คำอธิบาย ราคา หน้ารายละเอียด Checkout และ Order summary
- [x] บันทึกออเดอร์จริงใน Supabase เริ่มที่ PENDING
- [x] ปุ่มชำระเงินจำลองมีคำว่า DEMO ONLY และเปลี่ยนเป็น PAID
- [x] ค้นหาด้วยหมายเลขออเดอร์ + อีเมล และไม่เปิดข้อมูลด้วย ID อย่างเดียว
- [x] ออเดอร์ PAID ได้ signed URL อายุ 15 นาทีจาก bucket private
- [x] แสดงสถานะและตัวอย่างอีเมลจำลองสำเร็จอย่างชัดเจน (ไม่ส่งจริง)
- [x] เปิด RLS; anon อ่านได้เฉพาะหนังสือ และอ่าน orders ไม่ได้
- [x] Secret key อยู่ server environment เท่านั้น
- [x] Production บน Vercel: https://vibecode-gamma-murex.vercel.app
- [x] Source บน GitHub: https://github.com/bfirstkok/lumishelf-vibe-ebook-2026
- [x] MIT App Inventor WebViewer: FollowLinks=true, IgnoreSslErrors=false, UsesLocation=false
- [x] Back: GoBack เมื่อมี history มิฉะนั้นปิดหน้าจอ
- [x] Build APK สำเร็จและติดตั้งบน Android Emulator สำเร็จ
- [x] Production automated flow ผ่าน 15/15 รายการ (`production-test-results.json`)

หมายเหตุ: ใบงานอนุญาตผลการส่งอีเมลแบบจำลองที่มองเห็นได้สำหรับการทดสอบ โครงงานนี้เลือกวิธีดังกล่าว จึงไม่มีการส่งอีเมลจริงและไม่มีการรับเงินจริง
