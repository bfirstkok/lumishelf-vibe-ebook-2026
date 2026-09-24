import styles from "./page.module.css";

const products = [
  {
    title: "eBook: Productivity Hacks",
    price: "฿199",
    image: "https://raw.githubusercontent.com/bfirstkok/lumishelf-vibe-ebook-2026/main/assets/ebook-illustrations/small-systems-better-life.png",
  },
  {
    title: "Notion Student Planner",
    price: "฿199",
    image: "https://raw.githubusercontent.com/bfirstkok/lumishelf-vibe-ebook-2026/main/assets/ebook-illustrations/coffee-and-rain.png",
  },
  {
    title: "Source Code: Web Portfolio",
    price: "฿349",
    image: "https://raw.githubusercontent.com/bfirstkok/lumishelf-vibe-ebook-2026/main/assets/ebook-illustrations/sqlite-task-manager-pro.png",
  },
  {
    title: "คอร์ส Python พื้นฐาน",
    price: "฿890",
    image: "https://raw.githubusercontent.com/bfirstkok/lumishelf-vibe-ebook-2026/main/assets/ebook-illustrations/media-player-pro.png",
  },
];

const colors = [
  ["Sakura Pink", "#FF5CA8"],
  ["Sky Blue", "#5AA7FF"],
  ["Lavender", "#9A7BFF"],
  ["Cream", "#FFF9F2"],
  ["Mint", "#7ADFC9"],
];

export default function DigiHubDesignPage() {
  return (
    <main className={styles.page}>
      <section className={styles.hero}>
        <div className={styles.petals}>✿　✦　❀　✿</div>
        <div className={styles.heroCopy}>
          <div className={styles.badge}>DIGIHUB / デジハブ · MINI PROJECT</div>
          <h1>Japanese Anime Digital Store</h1>
          <p className={styles.lead}>
            แนวคิดการออกแบบร้านค้าสินค้าดิจิทัลที่ผสมความเป็นญี่ปุ่น โทนซากุระ
            และกลิ่นอาย Anime เข้ากับ UI ที่ใช้งานง่าย ดูทันสมัย และมีเอกลักษณ์
          </p>
          <div className={styles.heroTags}>
            <span>Web App</span>
            <span>Desktop App</span>
            <span>Mobile App</span>
          </div>
        </div>
        <div className={styles.heroArt}>
          <div className={styles.miniWindow}>
            <div className={styles.windowTop}>
              <span></span><span></span><span></span>
            </div>
            <div className={styles.mascotWrap}>
              <div className={styles.mascot}>ฅ^•ﻌ•^ฅ</div>
              <div>
                <b>DigiHub</b>
                <small>Digital Ideas, Japanese Inspiration</small>
              </div>
            </div>
            <div className={styles.heroCards}>
              <div className={styles.heroCard}>eBook</div>
              <div className={styles.heroCard}>Template</div>
              <div className={styles.heroCard}>Source Code</div>
            </div>
          </div>
        </div>
      </section>

      <section className={styles.section}>
        <div className={styles.sectionTitle}>
          <span>01</span>
          <div>
            <h2>คอนเซ็ปต์การออกแบบร้านค้า</h2>
            <p>Concept & Visual Direction</p>
          </div>
        </div>
        <div className={styles.twoCol}>
          <article className={styles.card}>
            <h3>แนวคิดหลัก</h3>
            <p>
              DigiHub เป็นร้านค้าสินค้าดิจิทัลสำหรับ eBook, Template, Source Code,
              Online Course และ Design Assets โดยใช้ธีมญี่ปุ่น–Anime
              เพื่อสร้างบรรยากาศที่เป็นมิตร สดใส และจดจำง่าย
            </p>
            <p>
              ดีไซน์เน้นความสมดุลระหว่างความน่ารักแบบ Kawaii กับโครงสร้าง UI
              ที่เป็นระบบ เพื่อให้ผู้ใช้ค้นหา เลือกซื้อ ชำระเงิน
              และดาวน์โหลดสินค้าได้โดยไม่สับสน
            </p>
          </article>
          <article className={styles.card}>
            <h3>Design Keywords</h3>
            <div className={styles.keywordGrid}>
              {["Sakura", "Anime", "Kawaii", "Clean UI", "Rounded", "Soft Shadow", "Japanese Accent", "Cross-platform"].map((item) => (
                <span key={item}>{item}</span>
              ))}
            </div>
          </article>
        </div>
      </section>

      <section className={styles.section}>
        <div className={styles.sectionTitle}>
          <span>02</span>
          <div>
            <h2>Design System</h2>
            <p>Color, Shape & Interface Language</p>
          </div>
        </div>
        <div className={styles.colorGrid}>
          {colors.map(([name, hex]) => (
            <div className={styles.colorCard} key={name}>
              <div className={styles.swatch} style={{ background: hex }}></div>
              <b>{name}</b>
              <code>{hex}</code>
            </div>
          ))}
        </div>
        <div className={styles.designNotes}>
          <div><b>Typography</b><span>ตัวอักษรอ่านง่าย น้ำหนักชัดเจน ใช้ภาษาไทยเป็นหลัก และมี Japanese Accent เล็กน้อย</span></div>
          <div><b>Components</b><span>Rounded Card, Pill Button, Soft Shadow, Search Bar, Product Card, Sidebar และ Bottom Navigation</span></div>
          <div><b>Illustration</b><span>ใช้ภาพประกอบสไตล์ญี่ปุ่น/Anime ใน Hero และ Thumbnail เพื่อสร้างเอกลักษณ์ แต่ไม่รบกวนการอ่านข้อมูล</span></div>
        </div>
      </section>

      <section className={styles.section}>
        <div className={styles.sectionTitle}>
          <span>03</span>
          <div>
            <h2>ตัวอย่างหน้าร้านและสินค้า</h2>
            <p>Storefront Preview</p>
          </div>
        </div>
        <div className={styles.storePreview}>
          <div className={styles.storeNav}>
            <b>DigiHub <em>デジハブ</em></b>
            <div className={styles.search}>ค้นหาสินค้า เช่น eBook, Template, คอร์สเรียน...</div>
            <span>🛒 3</span>
          </div>
          <div className={styles.storeHero}>
            <div>
              <small>DIGITAL PRODUCTS FOR A BRIGHTER TOMORROW</small>
              <h3>ค้นพบสินค้าดิจิทัลที่ใช่<br /><strong>เริ่มสร้างได้ทันที</strong></h3>
              <p>แหล่งรวมสินค้าดิจิทัลสำหรับนักเรียน นักพัฒนา และครีเอเตอร์</p>
              <button>เลือกดูสินค้า →</button>
            </div>
            <div className={styles.sakuraPanel}>
              <span>🌸</span>
              <b>アイデアを<br/>かたちに</b>
              <small>Turn ideas into something real.</small>
            </div>
          </div>
          <div className={styles.productGrid}>
            {products.map((product) => (
              <article className={styles.productCard} key={product.title}>
                <div className={styles.productImageWrap}>
                  <img src={product.image} alt={product.title} />
                </div>
                <h4>{product.title}</h4>
                <p>สินค้าดิจิทัลคุณภาพ พร้อมดาวน์โหลดหลังชำระเงิน</p>
                <div className={styles.productBottom}>
                  <b>{product.price}</b>
                  <button>เพิ่มลงตะกร้า</button>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className={styles.section}>
        <div className={styles.sectionTitle}>
          <span>04</span>
          <div>
            <h2>การออกแบบทั้ง 3 แพลตฟอร์ม</h2>
            <p>Responsive Experience</p>
          </div>
        </div>
        <div className={styles.platformGrid}>
          <article className={styles.platformCard}>
            <div className={styles.desktopMock}>
              <div className={styles.mockBar}></div>
              <div className={styles.mockHero}></div>
              <div className={styles.mockRows}><i></i><i></i><i></i></div>
            </div>
            <h3>Web App</h3>
            <p>Navbar ด้านบน พื้นที่แสดงสินค้ากว้าง เหมาะกับการเลือกดูและเปรียบเทียบสินค้า</p>
          </article>
          <article className={styles.platformCard}>
            <div className={styles.desktopMock}>
              <div className={styles.sidebarMock}></div>
              <div className={styles.desktopContent}>
                <div className={styles.mockHero}></div>
                <div className={styles.mockRows}><i></i><i></i><i></i></div>
              </div>
            </div>
            <h3>Desktop App</h3>
            <p>ใช้ Sidebar เพื่อเข้าถึงสินค้า ดาวน์โหลด คำสั่งซื้อ และการตั้งค่าได้รวดเร็ว</p>
          </article>
          <article className={styles.platformCard}>
            <div className={styles.phoneMock}>
              <div className={styles.phoneTop}></div>
              <div className={styles.phoneHero}></div>
              <div className={styles.phoneGrid}><i></i><i></i><i></i><i></i></div>
              <div className={styles.phoneNav}></div>
            </div>
            <h3>Mobile App</h3>
            <p>ออกแบบสำหรับการสัมผัส ใช้ Bottom Navigation และ Product Card ขนาดเหมาะกับมือถือ</p>
          </article>
        </div>
      </section>

      <section className={styles.section}>
        <div className={styles.sectionTitle}>
          <span>05</span>
          <div>
            <h2>ฟีเจอร์หลักและ User Flow</h2>
            <p>Core Features</p>
          </div>
        </div>
        <div className={styles.flow}>
          {["Login / สมัครสมาชิก", "เลือกสินค้า", "รายละเอียดสินค้า", "เพิ่มลงตะกร้า", "ชำระเงิน", "ดาวน์โหลดสินค้า"].map((step, index) => (
            <div key={step} className={styles.flowItem}>
              <span>{index + 1}</span>
              <b>{step}</b>
            </div>
          ))}
        </div>
        <div className={styles.featureGrid}>
          {[
            ["🔎", "ค้นหาและหมวดหมู่", "ค้นหาสินค้าดิจิทัลได้รวดเร็ว"],
            ["🛒", "ตะกร้าสินค้า", "จัดการรายการก่อนชำระเงิน"],
            ["💳", "ชำระเงิน", "ออกแบบขั้นตอน Checkout ให้เข้าใจง่าย"],
            ["⬇️", "ดาวน์โหลด", "รับไฟล์ดิจิทัลได้ทันที"],
            ["📦", "ประวัติคำสั่งซื้อ", "ตรวจสอบรายการซื้อย้อนหลัง"],
            ["🛠️", "Admin", "จัดการสินค้าและคำสั่งซื้อ"],
          ].map(([icon, title, desc]) => (
            <article className={styles.featureCard} key={title}>
              <span>{icon}</span>
              <div><b>{title}</b><p>{desc}</p></div>
            </article>
          ))}
        </div>
      </section>

      <section className={styles.footer}>
        <div>
          <div className={styles.footerLogo}>DigiHub <span>デジハブ</span></div>
          <p>Digital Ideas, Japanese Inspiration.</p>
        </div>
        <div className={styles.footerNote}>
          <b>Mini Project — UI Design</b>
          <span>Web · Desktop · Mobile</span>
        </div>
      </section>
    </main>
  );
}
