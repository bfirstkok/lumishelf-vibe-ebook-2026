export type Book = {
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  description: string;
  price: number;
  category: string;
  pages: number;
  accent: string;
  cover: string;
  filePath: string;
};

export const books: Book[] = [
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655104",
    slug: "media-player-pro",
    title: "Media Player PRO",
    subtitle: "สร้างเครื่องเล่นสื่อสไตล์อนิเมะด้วย PyQt6",
    description: "คู่มือ Sakura Beats จากใบงานเดิม พร้อมภาพแอปจริง วิธีจัด Playlist ควบคุมเพลง ใช้ Favorite และทดสอบธีมอนิเมะกับแอนิเมชันปุ่ม",
    price: 199,
    category: "Desktop Development",
    pages: 6,
    accent: "#ec79b9",
    cover: "/covers/media-player-pro.svg",
    filePath: "media-player-pro.pdf",
  },
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655105",
    slug: "tarot-app",
    title: "Tarot App",
    subtitle: "ออกแบบแอปไพ่ทาโรต์ที่มีเรื่องราวในทุกใบ",
    description: "เรียนรู้แนวคิดการสร้างแอปสุ่มไพ่ทาโรต์ การจัดข้อมูลไพ่ การแสดงคำอธิบาย และการออกแบบหน้าจอเปิดไพ่ให้ชวนติดตาม",
    price: 179,
    category: "Creative Coding",
    pages: 6,
    accent: "#ba8ef1",
    cover: "/covers/tarot-app.svg",
    filePath: "tarot-app.pdf",
  },
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655106",
    slug: "sqlite-task-manager-pro",
    title: "SQLite Task Manager PRO",
    subtitle: "เปลี่ยนรายการงานให้เป็นแอปจัดการที่ใช้ง่าย",
    description: "คู่มือออกแบบแอปจัดการงานด้วย SQLite ครอบคลุมการเพิ่ม แก้ไข ลบ ค้นหา กรองสถานะ และจัดหน้าจอให้เห็นสิ่งที่ต้องทำได้ชัดเจน",
    price: 229,
    category: "Database & Productivity",
    pages: 6,
    accent: "#54d6c0",
    cover: "/covers/sqlite-task-manager-pro.svg",
    filePath: "sqlite-task-manager-pro.pdf",
  },
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655101",
    slug: "city-where-stars-sleep",
    title: "เมืองที่ดาวหลับใหล",
    subtitle: "เมื่อความทรงจำส่องสว่างกว่าท้องฟ้า",
    description: "นิยายสั้นภาพประกอบแบบสไลด์ ว่าด้วยนักซ่อมโคมไฟและเมืองที่กลับมาฟังความทรงจำของกันและกัน",
    price: 189,
    category: "Fantasy",
    pages: 4,
    accent: "#7c6cff",
    cover: "/covers/stars.svg",
    filePath: "city-where-stars-sleep.pdf",
  },
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655102",
    slug: "small-systems-better-life",
    title: "ออกแบบชีวิตด้วยระบบเล็ก ๆ",
    subtitle: "ไม่ต้องเก่งขึ้นทุกวัน แค่เริ่มให้ง่ายกว่าเดิม",
    description: "คู่มือภาพประกอบแบบสไลด์ เริ่มนิสัยจากขั้นเล็ก ๆ ลดแรงตัดสินใจ และทบทวนระบบให้พอดีกับชีวิต",
    price: 229,
    category: "Self growth",
    pages: 4,
    accent: "#ff8f70",
    cover: "/covers/systems.svg",
    filePath: "small-systems-better-life.pdf",
  },
  {
    id: "0e29aa06-89e1-4f29-a351-a0f62e655103",
    slug: "coffee-and-rain",
    title: "กาแฟหนึ่งแก้วกับฤดูฝน",
    subtitle: "เรื่องสั้นสำหรับวันที่ใจต้องการที่พัก",
    description: "เรื่องสั้นภาพประกอบแบบสไลด์ เมื่อคนแปลกหน้าหลบฝนเข้าร้านกาแฟก่อนปิด และพบความกล้าสำหรับการเริ่มใหม่",
    price: 159,
    category: "Slice of life",
    pages: 4,
    accent: "#36c3a1",
    cover: "/covers/rain.svg",
    filePath: "coffee-and-rain.pdf",
  },
];

export const getBook = (slugOrId: string) =>
  books.find((book) => book.slug === slugOrId || book.id === slugOrId);

export const formatBaht = (price: number) =>
  new Intl.NumberFormat("th-TH", { style: "currency", currency: "THB", maximumFractionDigits: 0 }).format(price);
