-- Optional catalog update for an existing Supabase database.
-- Run after schema.sql. Does not modify existing books or orders.
insert into public.books (id, slug, title, subtitle, description, price, category, pages, cover_url, file_path)
values
('0e29aa06-89e1-4f29-a351-a0f62e655104','media-player-pro','Media Player PRO','สร้างเครื่องเล่นสื่อสไตล์อนิเมะด้วย PyQt6','คู่มือโปรเจกต์เครื่องเล่นเพลงและวิดีโอ ตั้งแต่การจัด Playlist ปุ่มควบคุมสื่อ ไปจนถึงธีมญี่ปุ่นและแอนิเมชันตอบสนองการกดปุ่ม',199,'Desktop Development',32,'/covers/media-player-pro.svg','media-player-pro.pdf'),
('0e29aa06-89e1-4f29-a351-a0f62e655105','tarot-app','Tarot App','ออกแบบแอปไพ่ทาโรต์ที่มีเรื่องราวในทุกใบ','เรียนรู้แนวคิดการสร้างแอปสุ่มไพ่ทาโรต์ การจัดข้อมูลไพ่ การแสดงคำอธิบาย และการออกแบบหน้าจอเปิดไพ่ให้ชวนติดตาม',179,'Creative Coding',28,'/covers/tarot-app.svg','tarot-app.pdf'),
('0e29aa06-89e1-4f29-a351-a0f62e655106','sqlite-task-manager-pro','SQLite Task Manager PRO','เปลี่ยนรายการงานให้เป็นแอปจัดการที่ใช้ง่าย','คู่มือออกแบบแอปจัดการงานด้วย SQLite ครอบคลุมการเพิ่ม แก้ไข ลบ ค้นหา กรองสถานะ และจัดหน้าจอให้เห็นสิ่งที่ต้องทำได้ชัดเจน',229,'Database & Productivity',36,'/covers/sqlite-task-manager-pro.svg','sqlite-task-manager-pro.pdf')
on conflict (id) do nothing;
