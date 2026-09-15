from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, NextPageTemplate, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle
)

ROOT = Path(r"D:\code\select topic software\vibecode")
OUT = ROOT / "docs" / "VibeCoding_EbookShop_Report.pdf"
FONT = Path(r"C:\Windows\Fonts\tahoma.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\tahomabd.ttf")
pdfmetrics.registerFont(TTFont("Tahoma", str(FONT)))
pdfmetrics.registerFont(TTFont("Tahoma-Bold", str(FONT_BOLD)))

INK = colors.HexColor("#18211F")
VIOLET = colors.HexColor("#7668E8")
PAPER = colors.HexColor("#F6F2E9")
CREAM = colors.HexColor("#FFFDF7")
MUTED = colors.HexColor("#66706C")
MINT = colors.HexColor("#34B99A")
CORAL = colors.HexColor("#F28B70")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Thai", fontName="Tahoma", fontSize=10, leading=17, textColor=INK))
styles.add(ParagraphStyle(name="ThaiSmall", fontName="Tahoma", fontSize=8, leading=13, textColor=MUTED))
styles.add(ParagraphStyle(name="ThaiBold", fontName="Tahoma-Bold", fontSize=10, leading=16, textColor=INK))
styles.add(ParagraphStyle(name="WhiteBold", fontName="Tahoma-Bold", fontSize=9, leading=14, textColor=colors.white))
styles.add(ParagraphStyle(name="H1Thai", fontName="Tahoma-Bold", fontSize=27, leading=36, textColor=INK, spaceAfter=10))
styles.add(ParagraphStyle(name="H2Thai", fontName="Tahoma-Bold", fontSize=18, leading=25, textColor=INK, spaceBefore=6, spaceAfter=11))
styles.add(ParagraphStyle(name="Label", fontName="Tahoma-Bold", fontSize=7.5, leading=11, textColor=VIOLET, tracking=1.5))
styles.add(ParagraphStyle(name="CoverTitle", fontName="Tahoma-Bold", fontSize=38, leading=49, textColor=colors.white, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="CoverSub", fontName="Tahoma", fontSize=13, leading=22, textColor=colors.HexColor("#D8E0DD")))
styles.add(ParagraphStyle(name="Center", parent=styles["Thai"], alignment=TA_CENTER))

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFont("Tahoma-Bold", 8)
    canvas.setFillColor(INK)
    canvas.drawString(18*mm, A4[1]-13*mm, "LumiShelf · Vibe Coding E-book Shop 2026")
    canvas.setStrokeColor(colors.HexColor("#DDD7CC"))
    canvas.line(18*mm, A4[1]-17*mm, A4[0]-18*mm, A4[1]-17*mm)
    canvas.setFont("Tahoma", 8)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(A4[0]-18*mm, 11*mm, f"หน้า {doc.page}")
    canvas.restoreState()

def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(VIOLET)
    canvas.circle(A4[0]-30*mm, A4[1]-48*mm, 55*mm, fill=1, stroke=0)
    canvas.setFillColor(CORAL)
    canvas.circle(18*mm, 25*mm, 28*mm, fill=1, stroke=0)
    canvas.setFont("Tahoma", 8)
    canvas.setFillColor(colors.white)
    canvas.drawString(18*mm, 13*mm, "จัดทำวันที่ 14 กันยายน 2026 · DEMO ONLY")
    canvas.restoreState()

doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=23*mm, bottomMargin=18*mm,
                      title="LumiShelf — Vibe Coding E-book Shop 2026")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
cover_frame = Frame(18*mm, 40*mm, A4[0]-36*mm, A4[1]-75*mm, id="cover")
doc.addPageTemplates([
    PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_page),
    PageTemplate(id="Body", frames=[frame], onPage=header_footer),
])

story = []
story += [Spacer(1, 48*mm), Paragraph("FINAL PROJECT REPORT", styles["Label"]), Spacer(1, 7*mm),
          Paragraph("LumiShelf<br/>ร้าน E-book ฉบับ Vibe Coding", styles["CoverTitle"]), Spacer(1, 8*mm),
          Paragraph("เว็บไซต์ฝั่งลูกค้า + Mock Payment + Order Tracking<br/>Next.js · Supabase · Resend · Vercel · MIT App Inventor", styles["CoverSub"]),
          Spacer(1, 22*mm)]
cover_box = Table([[Paragraph("PRODUCTION URL", styles["Label"]), Paragraph("https://vibecode-gamma-murex.vercel.app", styles["ThaiBold"])],
                   [Paragraph("STATUS", styles["Label"]), Paragraph("Build ผ่าน · Deploy แล้ว · Demo flow ใช้งานได้", styles["Thai"])]], colWidths=[38*mm, 115*mm])
cover_box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FFFFFF14")),("TEXTCOLOR",(0,0),(-1,-1),colors.white),
                               ("BOX",(0,0),(-1,-1),.6,colors.HexColor("#FFFFFF40")),("INNERGRID",(0,0),(-1,-1),.4,colors.HexColor("#FFFFFF24")),
                               ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),
                               ("TOPPADDING",(0,0),(-1,-1),11),("BOTTOMPADDING",(0,0),(-1,-1),11)]))
story += [cover_box, NextPageTemplate("Body"), PageBreak()]

story += [Paragraph("01 · ภาพรวมผลงาน", styles["Label"]), Paragraph("เว็บไซต์ร้านหนังสือดิจิทัลที่ใช้งานได้ครบ flow", styles["H1Thai"]),
          Paragraph("LumiShelf เป็นเว็บขาย E-book ฝั่งลูกค้าตามโจทย์ใบงาน มีหน้าเลือกหนังสือ รายละเอียด Checkout การสร้างเลขคำสั่งซื้อ Mock Payment การติดตามด้วยอีเมล และการดาวน์โหลดหลังสถานะ PAID โดยสื่อสารชัดเจนว่าเป็นระบบสาธิตและไม่มีการรับเงินจริง", styles["Thai"]), Spacer(1, 6*mm)]
reqs = [
    ("ผ่าน", "รายการหนังสือ", "3 เล่ม พร้อมปก ชื่อ คำอธิบาย ราคา หมวดหมู่ และจำนวนหน้า"),
    ("ผ่าน", "Checkout", "รับชื่อและอีเมล พร้อมสรุปคำสั่งซื้อก่อนยืนยัน"),
    ("ผ่าน", "Order", "สร้างเลขรูปแบบ LS-YYYYMMDD-XXXXX และสถานะเริ่มต้น PENDING"),
    ("ผ่าน", "Mock Payment", "แสดง DEMO ONLY ชัดเจน เปลี่ยนเป็น PAID โดยไม่มี QR/บัตร/เงินจริง"),
    ("ผ่าน", "Tracking", "ต้องกรอกเลขออเดอร์ร่วมกับอีเมล จึงไม่เปิดเผยคำสั่งซื้อของผู้อื่น"),
    ("ผ่าน", "Download", "ปุ่มดาวน์โหลดปรากฏหลัง PAID; Production รองรับ Signed URL อายุ 15 นาที"),
]
table_data = [[Paragraph("ผล",styles["WhiteBold"]),Paragraph("หัวข้อ",styles["WhiteBold"]),Paragraph("หลักฐานการทำงาน",styles["WhiteBold"])]] + [[Paragraph(a, styles["ThaiBold"]),Paragraph(b,styles["ThaiBold"]),Paragraph(c,styles["ThaiSmall"])] for a,b,c in reqs]
t = Table(table_data, colWidths=[12*mm,34*mm,116*mm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),INK),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#DDD7CC")),
                       ("BACKGROUND",(0,1),(0,-1),colors.HexColor("#E5F6F1")),("TEXTCOLOR",(0,1),(0,-1),MINT),("VALIGN",(0,0),(-1,-1),"TOP"),
                       ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
story += [t, Spacer(1,7*mm), Paragraph("ลิงก์โปรแกรม", styles["H2Thai"]), Paragraph("เปิดใช้งานได้ที่ <link href='https://vibecode-gamma-murex.vercel.app' color='#7668E8'><u>https://vibecode-gamma-murex.vercel.app</u></link> — โหมด Demo เก็บคำสั่งซื้อในเบราว์เซอร์ จึงทดลองได้ทันทีโดยไม่ต้องใส่คีย์", styles["Thai"]), PageBreak()]

story += [Paragraph("02 · USER INTERFACE", styles["Label"]), Paragraph("หน้าร้านและหน้ารายละเอียด", styles["H1Thai"]),
          Paragraph("ออกแบบ responsive ด้วยโทน editorial อบอุ่น ใช้ปก SVG ต้นฉบับ ลดการพึ่งพาทรัพย์สินภายนอก และมีแถบ DEMO ONLY บนทุกหน้า", styles["Thai"]), Spacer(1,4*mm)]
for image_name, caption in [("01-home.png", "หน้าแรก: Hero, คุณสมบัติ และชั้นหนังสือ 3 เล่ม"), ("02-book-detail.png", "หน้ารายละเอียด: ข้อมูลไฟล์ ราคา และปุ่มเลือกเล่ม")]:
    path = ROOT / "docs" / image_name
    img = Image(str(path), width=162*mm, height=112.5*mm)
    story += [KeepTogether([img, Spacer(1,2*mm), Paragraph(caption, styles["Center"])]), Spacer(1,5*mm)]
    if image_name == "01-home.png": story.append(PageBreak())
story += [PageBreak()]

story += [Paragraph("03 · CHECKOUT & ORDER FLOW", styles["Label"]), Paragraph("จากการเลือกหนังสือสู่ไฟล์ดาวน์โหลด", styles["H1Thai"]),
          Image(str(ROOT/"docs"/"03-checkout.png"), width=162*mm, height=112.5*mm), Spacer(1,4*mm),
          Paragraph("Checkout แบ่งข้อมูลลูกค้าและสรุปยอดอย่างชัดเจน มี validation ชื่อ/อีเมล และข้อความยืนยันว่าไม่มีการตัดเงินจริง", styles["Thai"]), Spacer(1,6*mm)]
flow = [[Paragraph("1",styles["ThaiBold"]),Paragraph("เลือกหนังสือ",styles["ThaiBold"]),Paragraph("เปิดรายละเอียดและยืนยันเล่ม",styles["ThaiSmall"])],
        [Paragraph("2",styles["ThaiBold"]),Paragraph("กรอก Checkout",styles["ThaiBold"]),Paragraph("ชื่อ + อีเมล + สรุปยอด",styles["ThaiSmall"])],
        [Paragraph("3",styles["ThaiBold"]),Paragraph("PENDING",styles["ThaiBold"]),Paragraph("ระบบสร้างเลขคำสั่งซื้อ",styles["ThaiSmall"])],
        [Paragraph("4",styles["ThaiBold"]),Paragraph("DEMO PAYMENT",styles["ThaiBold"]),Paragraph("กดจำลองชำระ ไม่มีธุรกรรมเงินจริง",styles["ThaiSmall"])],
        [Paragraph("5",styles["ThaiBold"]),Paragraph("PAID + DOWNLOAD",styles["ThaiBold"]),Paragraph("เปิดปุ่มดาวน์โหลด/ส่งอีเมลในโหมดจริง",styles["ThaiSmall"])]]
ft = Table(flow,colWidths=[13*mm,48*mm,101*mm])
ft.setStyle(TableStyle([("BACKGROUND",(0,0),(0,-1),VIOLET),("TEXTCOLOR",(0,0),(0,-1),colors.white),("BOX",(0,0),(-1,-1),.6,colors.HexColor("#D8D1C5")),
                        ("INNERGRID",(0,0),(-1,-1),.4,colors.HexColor("#E2DCD2")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
                        ("LEFTPADDING",(0,0),(-1,-1),8)]))
story += [ft, PageBreak()]

story += [Paragraph("04 · ARCHITECTURE & SECURITY", styles["Label"]), Paragraph("โครงสร้างที่พร้อมต่อ Production", styles["H1Thai"])]
arch = [[Paragraph("Browser",styles["WhiteBold"]),Paragraph("Next.js Server",styles["WhiteBold"]),Paragraph("Supabase / Resend",styles["WhiteBold"])],
        [Paragraph("หน้าเว็บและ publishable key เท่านั้น",styles["ThaiSmall"]),Paragraph("ตรวจข้อมูล, สร้าง/ค้นหาออเดอร์, สร้าง Signed URL",styles["ThaiSmall"]),Paragraph("Postgres + private Storage + ส่งอีเมล",styles["ThaiSmall"])]]
at=Table(arch,colWidths=[54*mm]*3)
at.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),INK),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.6,colors.HexColor("#D8D1C5")),
                        ("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),11),("BOTTOMPADDING",(0,0),(-1,-1),11),("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9)]))
story += [at, Spacer(1,7*mm), Paragraph("มาตรการสำคัญ",styles["H2Thai"])]
security = [
    "เปิด RLS บน books และ orders; anon อ่านได้เฉพาะหนังสือ active",
    "ไม่มี anon policy สำหรับ orders — ทุกการเข้าถึงผ่าน server route ที่ตรวจอีเมล",
    "SUPABASE_SECRET_KEY และ RESEND_API_KEY ไม่ถูกส่งไปฝั่ง browser",
    "Storage bucket ebooks เป็น private และสร้าง Signed URL อายุ 15 นาทีหลัง PAID",
    "Tracking query ใช้ order_number + customer_email เพื่อป้องกันข้อมูลรั่วไหล",
    "ไฟล์ .env ถูก ignore และมีเฉพาะ .env.example สำหรับโครงค่า",
]
for item in security: story += [Paragraph(f"<font color='#34B99A'>●</font>  {item}", styles["Thai"]), Spacer(1,1.5*mm)]
story += [Spacer(1,5*mm), Paragraph("ผลการทดสอบ",styles["H2Thai"]), Paragraph("npm test: ผ่าน 3/3 · npm run lint: ผ่าน · npm run build: ผ่าน · Browser flow: ผ่านตั้งแต่เลือกหนังสือถึง PAID และ Download · Vercel deployment: READY",styles["Thai"]), PageBreak()]

story += [Paragraph("05 · MOBILE & HANDOFF",styles["Label"]), Paragraph("MIT App Inventor WebViewer Wrapper",styles["H1Thai"]),
          Paragraph("จัดเตรียมไฟล์ LumiShelf-Production.aia ที่ตั้ง HomeUrl ไปยังเว็บ Production แล้ว พร้อม Block ปุ่ม Back: หากย้อนหน้าเว็บได้ให้ GoBack หากไม่ได้ให้ปิดหน้าจอ",styles["Thai"]), Spacer(1,5*mm)]
mobile = [[Paragraph("Property",styles["WhiteBold"]),Paragraph("Value",styles["WhiteBold"])],
          [Paragraph("HomeUrl",styles["Thai"]),Paragraph("https://vibecode-gamma-murex.vercel.app",styles["ThaiSmall"])],
          [Paragraph("FollowLinks",styles["Thai"]),Paragraph("True",styles["ThaiSmall"])],
          [Paragraph("IgnoreSslErrors",styles["Thai"]),Paragraph("False",styles["ThaiSmall"])],
          [Paragraph("UsesLocation",styles["Thai"]),Paragraph("False",styles["ThaiSmall"])],
          [Paragraph("Sizing",styles["Thai"]),Paragraph("Responsive",styles["ThaiSmall"])]]
mt=Table(mobile,colWidths=[56*mm,106*mm])
mt.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),INK),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#D8D1C5")),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),("LEFTPADDING",(0,0),(-1,-1),8)]))
story += [mt, Spacer(1,7*mm), Paragraph("ไฟล์สำคัญที่ส่งมอบ",styles["H2Thai"])]
files = ["README.md — วิธีเปิด/ตั้งค่า/deploy", "supabase/schema.sql — ตาราง seed RLS และ private bucket", "mobile/LumiShelf-Production.aia — โปรเจกต์ App Inventor", "docs/ — รายงาน เช็กลิสต์ และภาพหลักฐาน", "DEPLOYMENT_URL.txt — ลิงก์โปรแกรม"]
for item in files: story += [Paragraph(f"• {item}",styles["Thai"])]
story += [Spacer(1,8*mm), Paragraph("ขั้นตอนที่เจ้าของงานต้องทำเพิ่ม",styles["H2Thai"]),
          Paragraph("1) หากต้องการฐานข้อมูล/อีเมลจริง ให้ใส่ Supabase และ Resend credentials ตาม .env.example  2) Import ไฟล์ .aia ที่ ai2.appinventor.mit.edu แล้ว Build → Android App (.apk)  3) อัปโหลดโฟลเดอร์งานและ APK ไป Google Drive แล้วตั้งสิทธิ์ทุกคนที่มีลิงก์ดูได้",styles["Thai"]),
          Spacer(1,12*mm), Paragraph("หมายเหตุ: การ Build APK จำเป็นต้องใช้ระบบลงนามของบัญชี MIT App Inventor เจ้าของงาน จึงจัดเตรียม .aia ที่พร้อม Build ไว้ให้แล้ว",styles["ThaiSmall"])]

doc.build(story)
print(OUT)
