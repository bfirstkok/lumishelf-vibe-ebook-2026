from pathlib import Path
from html import escape
import json, re
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
OUT = ROOT / 'private' / 'ebooks'
OUT.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Thai', 'C:/Windows/Fonts/tahoma.ttf'))
pdfmetrics.registerFont(TTFont('ThaiBold', 'C:/Windows/Fonts/tahomabd.ttf'))
body = ParagraphStyle('body', fontName='Thai', fontSize=11, leading=20, wordWrap='CJK', spaceAfter=8)
title = ParagraphStyle('title', fontName='ThaiBold', fontSize=27, leading=36, wordWrap='CJK', spaceAfter=18, textColor=colors.HexColor('#7668e8'))
heading = ParagraphStyle('heading', fontName='ThaiBold', fontSize=15, leading=25, wordWrap='CJK', spaceAfter=12)
small = ParagraphStyle('small', fontName='Thai', fontSize=9, leading=15, wordWrap='CJK', spaceAfter=7)
compact = ParagraphStyle('compact', fontName='Thai', fontSize=7.2, leading=10.5, wordWrap='CJK', spaceAfter=3)

def p(text, style=body):
    return Paragraph(escape(text), style)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#ded9ce'))
    canvas.line(44,40,551,40)
    canvas.setFont('Thai',8)
    canvas.drawString(44,26,'LumiShelf | คู่มือประกอบโครงงานเพื่อการศึกษา')
    canvas.drawRightString(551,26,str(doc.page))
    canvas.restoreState()

projects = [
    ('media-player-pro','Media Player PRO','01_Media_Player_PRO','ui-preview-anime.png',
     'Sakura Beats: เครื่องเล่นเพลงธีม Anime Night Edition',
     ['เปิดโปรแกรมแล้วกดเพิ่มเพลง เลือกไฟล์เสียงที่มีสิทธิ์ใช้งานหลายไฟล์ เพลงจะปรากฏใน Playlist ดับเบิลคลิกรายการเพื่อเริ่มเล่น',
      'ใช้ Play/Pause เพื่อหยุดชั่วคราวและเล่นต่อ ใช้ Stop เมื่อต้องการเริ่มใหม่ เลื่อนแถบเวลาเพื่อข้ามตำแหน่ง ปรับระดับเสียงหรือปิดเสียงตามต้องการ',
      'ลองเปิด Shuffle แล้วใช้ Next จากนั้นเลือก Repeat เพลงเดียวหรือทั้งรายการ เปรียบเทียบพฤติกรรมเมื่อเพลงจบ',
      'กด Favorite เพื่อทำเครื่องหมายเพลง ใช้ช่องค้นหาและตัวกรองเพลงโปรด คลังเพลงสามารถซ่อนได้เพื่อเพิ่มพื้นที่หน้าเล่น',
      'ส่งออก Playlist เป็น M3U8 แล้วนำเข้ากลับ ไฟล์รายการอ้างอิงตำแหน่งเพลง ไม่ได้บรรจุไฟล์เพลงไว้ด้วย จึงต้องเก็บเพลงในตำแหน่งที่เข้าถึงได้'],
     'แยกสถานะการเล่นออกจากเอฟเฟกต์หน้าจอ ปุ่มและ slider ส่งคำสั่งไปยังตัวเล่น ขณะที่เหตุการณ์จากตัวเล่นอัปเดตเวลาและชื่อเพลง แอนิเมชันไม่ควรเป็นตัวกำหนดว่าเพลงกำลังเล่นหรือหยุด'),
    ('tarot-app','Tarot App PRO','02_Tarot_App_PRO','ui-preview.png',
     'ไพ่สามใบสำหรับอดีต ปัจจุบัน และอนาคต',
     ['เปิดแอปและเริ่มเปิดไพ่ จะเห็นไพ่สามตำแหน่งสำหรับอดีต ปัจจุบัน และอนาคต อ่านชื่อและคำอธิบายแยกตามตำแหน่ง',
      'กดเปิดไพ่รอบใหม่หลายครั้ง ไพ่ภายในรอบเดียวกันต้องไม่ซ้ำกัน แต่สามารถพบไพ่เดิมในคนละรอบได้ตามผลการสุ่ม',
      'เลือกไฟล์เพลงประกอบจากเครื่อง แล้วลองเล่น พัก หยุด และปรับระดับเสียง ไพ่ยังคงใช้งานได้แม้ไม่ได้เลือกเพลง',
      'หากรูปไพ่หายไป แอปควรแสดงภาพสำรองหรือข้อความที่เข้าใจได้โดยไม่ปิดตัวเอง ตรวจว่าภาพ ชื่อ และความหมายมาจากข้อมูลไพ่ใบเดียวกัน',
      'ใช้ข้อความไพ่เพื่อความบันเทิงและการสะท้อนความคิด ไม่ใช้เป็นข้อพิสูจน์อนาคตหรือทดแทนคำแนะนำจากผู้เชี่ยวชาญ'],
     'cards.py เก็บข้อมูลไพ่ ส่วน main.py จัดการหน้าต่างและเหตุการณ์ การสุ่มแบบไม่คืนค่าภายในหนึ่งรอบทำให้ได้ไพ่สามใบไม่ซ้ำกัน การทดสอบควรตรวจคุณสมบัตินี้แทนการบังคับชื่อไพ่ที่สุ่มได้'),
    ('sqlite-task-manager-pro','SQLite Task Manager PRO','03_SQLite_Task_Manager_PRO','ui-preview-pro.png',
     'Focus Flow: จัดการงานและเก็บข้อมูลด้วย SQLite',
     ['เข้าสู่ระบบสาธิตตามคู่มือในโปรเจกต์ แล้วเพิ่มงานที่มีชื่อชัดเจน ระบุหมวดหมู่ ความสำคัญ และกำหนดส่งให้เหมาะกับงาน',
      'ลอง Quick Add และเปลี่ยนสถานะจากยังไม่เริ่มเป็นกำลังทำ จากนั้นเสร็จแล้ว ตรวจว่าตาราง บอร์ด และตัวเลขสรุปเปลี่ยนสอดคล้องกัน',
      'ใช้ช่องค้นหาและตัวกรองเพื่อหางานที่ต้องทำวันนี้ ปักงานโปรด และตั้งเวลาคาดการณ์ โหมดโฟกัสมี Pomodoro 25 นาที',
      'ส่งออกข้อมูลเป็น CSV หรือ JSON ก่อนทดลองนำเข้าไฟล์ ตรวจหัวตารางและรูปแบบวันที่ หากข้อมูลไม่ถูกต้องต้องแจ้งข้อผิดพลาดที่แก้ไขได้',
      'ทดลองย้ายงานไปถังขยะและกู้คืน จากนั้นปิดเปิดโปรแกรมเพื่อตรวจการบันทึก สำรองฐานข้อมูลก่อนกู้คืน เพราะการ restore อาจแทนที่ข้อมูลปัจจุบัน'],
     'database.py แยกการจัดเก็บข้อมูลออกจาก GUI ใช้คำสั่ง SQL แบบมีพารามิเตอร์สำหรับค่าจากผู้ใช้ รหัสผ่านเก็บเป็น PBKDF2 hash พร้อม salt ข้อมูลสถานะและวันเสร็จต้องเปลี่ยนร่วมกันเพื่อให้ Dashboard คำนวณได้ถูกต้อง'),
]

counts = {}
for slug,name,folder,shot,subtitle,steps,architecture in projects:
    src = BASE / folder
    story = [Spacer(1,65),p('LUMISHELF / PROJECT GUIDE',small),p(name,title),p(subtitle,heading),
             p('คู่มือจากใบงาน Desktop Application AI Agent PyQt6'),
             p('เนื้อหาเรียบเรียงจาก README ข้อกำหนด และเอกสารออกแบบของโปรเจกต์เดิม ภาพหน้าจอเป็นหลักฐานที่จัดเก็บในโฟลเดอร์งาน'),
             p('สารบัญ: ภาพรวม / หน้าจอ / วิธีใช้ / ข้อกำหนด / การพัฒนาและตรวจสอบ / ที่มา',small),PageBreak(),
             p('01 / หน้าจอและจุดเริ่มต้น',heading)]
    shotpath=src/'docs'/shot
    if shotpath.exists():
        img=Image(str(shotpath)); img._restrictSize(490,365); story += [img,Spacer(1,15)]
    story += [p('หน้าจอของโปรเจกต์เดิม ใช้ประกอบคำอธิบายตำแหน่งการทำงาน ไม่ใช่ภาพทดสอบใหม่ในวันที่จัดทำหนังสือ',small),p(subtitle),PageBreak(),p('02 / วิธีใช้งานทีละขั้น',heading)]
    for i,step in enumerate(steps,1): story += [p(f'{i}. {step}'),Spacer(1,8)]
    story += [PageBreak(),p('03 / ข้อกำหนดจากใบงานเดิม',heading)]
    req=(src/'docs'/'01_REQUIREMENTS.md').read_text(encoding='utf-8-sig')
    for line in req.splitlines():
        if line.strip(): story.append(p(re.sub(r'^[#]+\s*','',line.replace('`','')),compact))
    story += [PageBreak(),p('04 / แนวทางพัฒนาและทดสอบ',heading),p(architecture),
              p('ทดสอบเส้นทางปกติก่อน จากนั้นทดสอบข้อมูลว่าง ไฟล์หาย หรือค่าที่ไม่ถูกต้อง โดยตรวจทั้งข้อความบนหน้าจอและข้อมูลหลังปิดเปิดโปรแกรม'),
              p('รันจาก source: เปิด terminal ในโฟลเดอร์แอป แล้วใช้ Python จาก virtual environment ที่ติดตั้ง PyQt6 รัน main.py',small),
              p('ทดสอบ: python -m unittest discover -s tests -v',small),
              p('Build โปรแกรม Windows: ใช้ build.ps1 ของโปรเจกต์ และส่งทั้งโฟลเดอร์ dist ของแอป ไม่ส่งเฉพาะ EXE หาก build แบบ onedir',small),
              p('การเปลี่ยน UI ควรตรวจว่าฟังก์ชันเดิมยังทำงาน โดยเฉพาะปุ่มที่มีแอนิเมชันและเหตุการณ์ที่เกิดระหว่างโหลดไฟล์'),
              PageBreak(),p('05 / อ้างอิงและไฟล์ประกอบ',heading),
              p(f'แหล่งข้อมูลในโฟลเดอร์งานเดิม: {folder}',small)]
    for f in ['README.md','docs/01_REQUIREMENTS.md','main.py','tests/','TEST_REPORT.md']:
        story.append(p(f,small))
    story += [p('ขอบเขตของหนังสือ',heading),p('หนังสือเป็นคู่มือประกอบแอปและแนวทางตรวจสอบ ไม่รวมเพลงเชิงพาณิชย์หรือข้อมูลส่วนตัว ไม่ใช่หนังสือสอนทุกบรรทัดของ source code'),
              p('แบบฝึกต่อยอด',heading),p('เลือกหนึ่งฟังก์ชันที่สนใจ อธิบาย input, output และ error case แล้วเพิ่มฟังก์ชันทีละส่วน ทดสอบก่อนและหลังการเปลี่ยน เพื่อให้เห็นผลอย่างตรวจสอบได้')]
    target=OUT/f'{slug}.pdf'
    SimpleDocTemplate(str(target),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=56,title=name).build(story,onFirstPage=footer,onLaterPages=footer)
    counts[slug]=len(PdfReader(target).pages)

# Three original catalog items are short, original sample texts.
samples=[
('city-where-stars-sleep','เมืองที่ดาวหลับใหล','นิยายสั้นต้นฉบับ',[
'ทุกคืน ลินจะเดินผ่านสถานีรถไฟที่ไม่มีขบวนใดจอดอยู่แล้ว เธอรับหน้าที่ซ่อมโคมไฟริมทาง แต่คืนหนึ่งกลับพบแสงเล็ก ๆ สั่นอยู่ในกล่องเครื่องมือ แสงนั้นไม่ส่องพื้น มันส่องภาพความทรงจำของคนที่เดินผ่าน',
'ชายขายขนมเห็นภาพจักรยานคันแรก เด็กนักเรียนเห็นมือที่เคยจับตนข้ามถนน ส่วนลินเห็นหน้าต่างห้องเก่าที่เปิดรอใครบางคน เธอเริ่มเข้าใจว่าเมืองไม่ได้มืดเพราะโคมไฟเสีย แต่เพราะผู้คนเลิกหยุดมองสิ่งที่ยังรัก',
'ลินไม่ได้ติดตั้งแสงนั้นบนยอดตึก เธอวางมันบนม้านั่งสถานี ทุกเย็นคนในเมืองผลัดกันมานั่งเล่าเรื่องที่เกือบลืม เมื่อรุ่งเช้ามาถึง กล่องว่างเปล่า แต่หน้าต่างแต่ละบ้านเริ่มมีแสงอุ่น ๆ อีกครั้ง ดาวของเมืองไม่ได้ตื่นบนฟ้า มันตื่นในบทสนทนาสั้น ๆ ระหว่างคนที่กลับมาฟังกัน']),
('small-systems-better-life','ออกแบบชีวิตด้วยระบบเล็ก ๆ','คู่มือสั้นต้นฉบับ',[
'เริ่มจากพฤติกรรมเดียวที่ทำซ้ำได้ เช่น หลังวางกระเป๋าให้เขียนงานสำคัญของพรุ่งนี้หนึ่งข้อ ระบบที่ดีลดแรงตัดสินใจ ไม่จำเป็นต้องบังคับให้ทุกวันมีประสิทธิภาพเท่ากัน',
'แบ่งงานให้มีขั้นเริ่มที่ใช้เวลาไม่เกินห้านาที หากอยากอ่านหนังสือให้เตรียมหน้าอ่านไว้ หากอยากเขียนรายงานให้เปิดไฟล์และเขียนหัวข้อแรก ใช้เวลาและพื้นที่เดิมเป็นตัวช่วยเตือน',
'ทบทวนสัปดาห์ละครั้งว่าอะไรช่วยและอะไรขัดขวาง หากพลาดหนึ่งวันให้กลับมาในขนาดเล็กลง อย่าใช้สถิติตัดสินคุณค่าของตัวเอง จดสิ่งที่ทำได้จริงและปรับระบบให้พอดีกับเวลาที่มี']),
('coffee-and-rain','กาแฟหนึ่งแก้วกับฤดูฝน','เรื่องสั้นต้นฉบับ',[
'ฝนเริ่มตกก่อนร้านปิดห้านาที เจ้าของร้านกำลังเก็บเก้าอี้เมื่อหญิงคนหนึ่งเดินเข้ามาพร้อมซองจดหมายที่เปียกมุมกระดาษ เธอสั่งน้ำเปล่าและถามว่านั่งรอให้ฝนหยุดได้ไหม',
'เขาวางผ้าแห้งข้างแก้ว เธอเล่าว่าซองนั้นเป็นใบตอบรับงานที่เมืองอื่น และเธอไม่แน่ใจว่าการเริ่มใหม่หมายถึงการทิ้งสิ่งเดิมหรือไม่ เจ้าของร้านมองเก้าอี้ที่ซื้อใหม่แทนตัวเก่าซึ่งขาหัก แล้วตอบว่าบางอย่างเปลี่ยนที่อยู่ แต่ความหมายยังอยู่กับเรา',
'เมื่อฝนซา เธอพับซองใส่กระเป๋าอย่างระวังและขอบคุณสำหรับน้ำหนึ่งแก้ว วันต่อมามีโปสการ์ดเล็ก ๆ สอดใต้ประตูร้าน เขียนเพียงว่าถึงสถานีทันแล้ว เจ้าของร้านติดมันไว้ข้างเครื่องชงกาแฟ เวลาฝนตก เขาจะเก็บเก้าอี้ช้าลงอีกห้านาที'])]
for slug,name,kind,paragraphs in samples:
    target=OUT/f'{slug}.pdf'
    story=[p(name,title),p(kind,heading)]+[p(x) for x in paragraphs]+[Spacer(1,20),p('ฉบับอ่านสั้นสำหรับร้านสาธิต LumiShelf เนื้อหานี้จัดทำขึ้นใหม่เพื่อเป็นไฟล์ดาวน์โหลดตัวอย่าง',small)]
    SimpleDocTemplate(str(target),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=56,title=name).build(story,onFirstPage=footer,onLaterPages=footer)
    counts[slug]=len(PdfReader(target).pages)
(OUT/'manifest.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(counts,ensure_ascii=False))
