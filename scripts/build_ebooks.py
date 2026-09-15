from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parent; OUT=ROOT/'private'/'ebooks'; ART=ROOT/'assets'/'ebook-illustrations'
OUT.mkdir(parents=True,exist_ok=True)
W,H=960,540
pdfmetrics.registerFont(TTFont('Thai','C:/Windows/Fonts/tahoma.ttf'));pdfmetrics.registerFont(TTFont('ThaiB','C:/Windows/Fonts/tahomabd.ttf'))

def hx(v): return colors.HexColor(v)
def wrap(text,font,size,width):
    lines=[]
    for para in text.split('\n'):
        words=para.split(' ');line=''
        for word in words:
            trial=(line+' '+word).strip()
            if pdfmetrics.stringWidth(trial,font,size)<=width: line=trial
            elif line:
                lines.append(line);line=word
            else:
                chunk=''
                for ch in word:
                    if pdfmetrics.stringWidth(chunk+ch,font,size)>width and chunk: lines.append(chunk);chunk=ch
                    else: chunk+=ch
                line=chunk
        if line: lines.append(line)
    return lines

def text(c,s,x,y,width,size=18,color='#25243A',font='Thai',leading=None,max_lines=99):
    c.setFont(font,size);c.setFillColor(hx(color));leading=leading or size*1.45
    for line in wrap(s,font,size,width)[:max_lines]: c.drawString(x,y,line);y-=leading
    return y

def rounded(c,x,y,w,h,fill='#FFFFFF',stroke=None,r=18):
    c.setFillColor(hx(fill));c.setStrokeColor(hx(stroke or fill));c.roundRect(x,y,w,h,r,fill=1,stroke=1 if stroke else 0)

def header(c,kicker,title,accent='#7668E8',dark=False):
    c.setFillColor(hx('#111327' if dark else '#F7F5FF'));c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(hx(accent));c.roundRect(44,482,122,25,12,fill=1,stroke=0)
    c.setFillColor(colors.white);c.setFont('ThaiB',10);c.drawCentredString(105,490,kicker)
    text(c,title,44,458,840,28,'#FFFFFF' if dark else '#23213A','ThaiB',38,2)

def footer(c,page,total,dark=False):
    c.setFillColor(hx('#A8A3BE' if dark else '#77728E'));c.setFont('Thai',8)
    c.drawString(44,22,'LumiShelf • E-book Visual Edition');c.drawRightString(916,22,f'{page:02d} / {total:02d}')

def image_fit(c,path,x,y,w,h):
    im=ImageReader(str(path));iw,ih=im.getSize();scale=min(w/iw,h/ih);dw,dh=iw*scale,ih*scale
    c.drawImage(im,x+(w-dw)/2,y+(h-dh)/2,dw,dh,mask='auto')

def cover(c,title,subtitle,art,accent,total):
    c.drawImage(ImageReader(str(art)),0,0,W,H,mask='auto')
    c.saveState();c.setFillAlpha(.74);c.setFillColor(hx('#101125'));c.roundRect(36,54,470,432,28,fill=1,stroke=0);c.restoreState()
    c.setFillColor(hx(accent));c.roundRect(72,420,142,28,14,fill=1,stroke=0)
    c.setFillColor(colors.white);c.setFont('ThaiB',10);c.drawCentredString(143,429,'LUMISHELF GUIDE')
    y=text(c,title,72,375,390,36,'#FFFFFF','ThaiB',44,3)
    y=text(c,subtitle,72,y-10,385,17,'#E9E7F9','Thai',25,4)
    c.setStrokeColor(hx(accent));c.setLineWidth(4);c.line(72,102,210,102)
    text(c,'ฉบับภาพประกอบ • อ่านง่ายแบบสไลด์',72,86,350,11,'#D9D6EC','Thai',16,2)
    footer(c,1,total,True);c.showPage()

def feature_cards(c,items,accent):
    for i,(name,desc) in enumerate(items):
        col=i%3;row=i//3;x=44+col*292;y=265-row*174
        rounded(c,x,y,270,142,'#FFFFFF','#E2DEF2',16);c.setFillColor(hx(accent));c.circle(x+28,y+108,14,fill=1,stroke=0)
        c.setFillColor(colors.white);c.setFont('ThaiB',10);c.drawCentredString(x+28,y+104,str(i+1))
        text(c,name,x+50,y+116,195,15,'#28243C','ThaiB',20,2);text(c,desc,x+20,y+75,230,10.5,'#625E73','Thai',16,4)

technical=[
dict(slug='media-player-pro',title='Media Player PRO',subtitle='Sakura Beats • เครื่องเล่นเพลงธีม Anime Night',accent='#EC79B9',folder='01_Media_Player_PRO',shot='ui-preview-anime.png',intro='เครื่องเล่นเพลงบน Desktop ที่รวม Playlist, Favorite และการควบคุมเสียงไว้ในหน้าจอเดียว พร้อมแอนิเมชันปุ่มที่ช่วยให้การใช้งานมีชีวิตชีวา',features=[('Playlist','เพิ่มหลายไฟล์ ค้นหา และจัดลำดับเพลง'),('Playback','Play, Pause, Stop, Next และแถบเวลา'),('Favorite','ทำเครื่องหมายเพลงโปรดและกรองได้ทันที'),('Modes','Shuffle และ Repeat เพลงเดียวหรือทั้งรายการ'),('Sound','ปรับระดับเสียง ปิดเสียง และความเร็ว 0.75–2x'),('Import / Export','บันทึกรายการเพลงเป็น M3U8 แล้วนำกลับมาใช้')],steps=['เลือกไฟล์เสียงที่มีสิทธิ์ใช้งาน','ตรวจชื่อเพลงใน Playlist','กดเล่นและลองเลื่อนเวลา','เลือก Shuffle หรือ Repeat','ส่งออก Playlist ก่อนปิดโปรแกรม'],arch=[('FILE','MP3 / WAV / FLAC'),('PLAYER','Qt Multimedia'),('STATE','Playlist + Favorite'),('UI','Anime controls')],tips=['ทดสอบปุ่มระหว่างกำลังโหลดไฟล์','Playlist อ้างพาธเพลง ไม่ได้บรรจุเพลง','แยกสถานะการเล่นออกจากแอนิเมชัน UI']),
dict(slug='tarot-app',title='Tarot App',subtitle='อดีต • ปัจจุบัน • อนาคต ผ่านไพ่สามใบ',accent='#BA8EF1',folder='02_Tarot_App_PRO',shot='ui-preview.png',intro='แอปเปิดไพ่สามตำแหน่งที่จัดข้อมูลภาพ ชื่อ และความหมายเป็นระบบ สุ่มไพ่ไม่ซ้ำกันภายในรอบ พร้อมเสียงประกอบที่เปิดหรือปิดได้',features=[('Three Cards','วางไพ่สำหรับอดีต ปัจจุบัน และอนาคต'),('Unique Draw','ไพ่สามใบในหนึ่งรอบไม่ซ้ำกัน'),('Meaning','ชื่อ ภาพ และคำอธิบายมาจากข้อมูลใบเดียวกัน'),('New Reading','สุ่มรอบใหม่ได้โดยไม่ต้องปิดแอป'),('Music','เล่น พัก หยุด และปรับเสียงประกอบ'),('Fallback','ภาพหายแล้วยังแจ้งผลได้โดยไม่ปิดตัวเอง')],steps=['ตั้งคำถามที่อยากทบทวน','กดเปิดไพ่รอบใหม่','อ่านความหมายทีละตำแหน่ง','สังเกตเรื่องร่วมของไพ่สามใบ','ใช้ผลเพื่อความบันเทิงและสะท้อนใจ'],arch=[('DATA','cards.py'),('RANDOM','sample 3 cards'),('VIEW','Card widgets'),('AUDIO','Optional music')],tips=['ทดสอบว่าไพ่ในรอบไม่ซ้ำ','รูปหายต้องมีภาพหรือข้อความสำรอง','ไม่ใช้คำทำนายแทนคำแนะนำผู้เชี่ยวชาญ']),
dict(slug='sqlite-task-manager-pro',title='SQLite Task Manager PRO',subtitle='Focus Flow • งาน ข้อมูล และเวลาที่อยู่ด้วยกัน',accent='#55C9B5',folder='03_SQLite_Task_Manager_PRO',shot='ui-preview-pro.png',intro='แอปจัดการงานที่เก็บข้อมูลใน SQLite มีสถานะ ความสำคัญ หมวดหมู่ Dashboard และ Pomodoro พร้อมเครื่องมือสำรองและนำเข้าข้อมูล',features=[('Tasks','เพิ่ม แก้ไข ทำซ้ำ และเปลี่ยนสถานะ'),('Views','ตาราง บอร์ด และ Dashboard สรุปภาพรวม'),('Search','ค้นหาและกรองหมวดหมู่หรือความสำคัญ'),('Focus','Pomodoro 25 นาทีและเวลาคาดการณ์'),('Safety','ถังขยะ กู้คืน และสำรองฐานข้อมูล'),('Exchange','นำเข้าและส่งออก CSV / JSON')],steps=['เข้าสู่ระบบสาธิต','เพิ่มงานพร้อมวันส่งและความสำคัญ','เปลี่ยนสถานะจาก To do ไป Doing','ใช้ Focus timer ระหว่างลงมือ','สำรองข้อมูลก่อน Restore'],arch=[('INPUT','Task form'),('LOGIC','Validation'),('DATABASE','SQLite'),('VIEW','Table + Board')],tips=['SQL ใช้พารามิเตอร์แทนการต่อสตริง','Password เก็บ PBKDF2 hash พร้อม salt','สถานะและวันเสร็จต้องเปลี่ยนสอดคล้องกัน'])]

def build_technical(d):
    out=OUT/(d['slug']+'.pdf');c=canvas.Canvas(str(out),pagesize=(W,H));art=ART/(d['slug']+'.png');total=6
    cover(c,d['title'],d['subtitle'],art,d['accent'],total)
    header(c,'01 • OVERVIEW','รู้จักแอปในหนึ่งหน้า',d['accent']);rounded(c,44,62,500,354,'#FFFFFF','#E2DEF2');image_fit(c,BASE/d['folder']/'docs'/d['shot'],62,82,464,314);text(c,d['intro'],580,380,330,17,'#312E48','ThaiB',27,6);text(c,'ภาพหน้าจอจริงจากโปรเจกต์เดิม',580,145,300,10,'#77728E','Thai',15,2);footer(c,2,total);c.showPage()
    header(c,'02 • FEATURES','ทำอะไรได้บ้าง',d['accent']);feature_cards(c,d['features'],d['accent']);footer(c,3,total);c.showPage()
    header(c,'03 • FLOW','เส้นทางการใช้งาน',d['accent']);
    for i,step in enumerate(d['steps']):
        x=55+i*177;rounded(c,x,205,150,150,'#FFFFFF','#DDD8EE',18);c.setFillColor(hx(d['accent']));c.circle(x+75,315,24,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('ThaiB',14);c.drawCentredString(x+75,310,str(i+1));text(c,step,x+15,270,120,11,'#343047','ThaiB',17,4)
        if i<4:c.setFillColor(hx(d['accent']));c.setFont('ThaiB',22);c.drawString(x+155,265,'›')
    text(c,'เคล็ดลับ: ทดลองเส้นทางปกติก่อน แล้วค่อยทดสอบไฟล์ว่าง ไฟล์หาย และค่าที่ไม่ถูกต้อง',80,150,800,14,'#5C5770','Thai',22,3);footer(c,4,total);c.showPage()
    header(c,'04 • ARCHITECTURE','เบื้องหลังแบบเห็นภาพ',d['accent']);
    for i,(a,b) in enumerate(d['arch']):
        x=55+i*220;rounded(c,x,220,185,130,'#FFFFFF','#DDD8EE',18);text(c,a,x+18,320,150,10,d['accent'],'ThaiB',14,1);text(c,b,x+18,282,150,14,'#29263D','ThaiB',21,3)
        if i<3:c.setFillColor(hx(d['accent']));c.setFont('ThaiB',24);c.drawString(x+194,270,'→')
    text(c,'แนวคิดสำคัญ: แยก Input, Logic, Storage และ View ทำให้แก้แต่ละส่วนได้โดยไม่ทำให้ทั้งแอปพัง',100,150,760,15,'#555066','Thai',24,3);footer(c,5,total);c.showPage()
    header(c,'05 • PRACTICE','ลองทำเองและตรวจงาน',d['accent']);rounded(c,44,80,560,335,'#FFFFFF','#DDD8EE',18)
    y=370
    for i,t in enumerate(d['tips'],1):c.setFillColor(hx(d['accent']));c.circle(78,y+2,12,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('ThaiB',9);c.drawCentredString(78,y-1,'✓');y=text(c,t,105,y+8,450,14,'#312E48','ThaiB',22,3)-25
    rounded(c,640,115,270,270,'#23223B');text(c,'CHECKLIST',670,345,200,11,d['accent'],'ThaiB',16,1);text(c,'□ เปิดโปรแกรมได้\n□ เส้นทางหลักทำงาน\n□ ข้อมูลยังอยู่หลังเปิดใหม่\n□ Error มีข้อความที่เข้าใจได้\n□ UI ไม่ค้างระหว่างทำงาน',670,310,205,13,'#FFFFFF','Thai',30,8);footer(c,6,total);c.save()

fiction=[
dict(slug='city-where-stars-sleep',title='เมืองที่ดาวหลับใหล',subtitle='เมื่อความทรงจำส่องสว่างกว่าท้องฟ้า',accent='#F2B45B',premise='ในเมืองริมแม่น้ำที่เก็บดาวไว้ในโคมแก้ว นักซ่อมโคมคนหนึ่งพบว่าดาวที่ดับไม่ได้หายไป แต่มันกำลังเก็บความทรงจำที่ผู้คนไม่กล้าพูดออกมา',beats=[('แสงที่หาย','โคมตามถนนเริ่มมืดลงทีละดวง'),('เสียงในโคม','ทุกดวงซ่อนความทรงจำของใครบางคน'),('คืนที่สว่าง','เมืองกลับมาฟังกันและกันอีกครั้ง')],ideas=['บางครั้งสิ่งที่ต้องซ่อมไม่ใช่แสง แต่คือการรับฟัง','ความทรงจำหนักได้ แต่แบ่งกันถือได้','การเริ่มพูดความจริงคือแสงดวงแรก']),
dict(slug='small-systems-better-life',title='ออกแบบชีวิตด้วยระบบเล็ก ๆ',subtitle='เริ่มให้ง่าย แล้วค่อยเติบโตอย่างยั่งยืน',accent='#86B89B',premise='เราไม่จำเป็นต้องพึ่งแรงฮึดทุกวัน ระบบที่ดีทำให้การเริ่มต้นเล็กพอที่จะลงมือ และชัดพอที่จะรู้ว่าวันนี้ทำสำเร็จแล้ว',beats=[('ลดแรงเริ่ม','วางอุปกรณ์หรือขั้นแรกไว้ให้เห็น'),('ผูกกับกิจวัตร','ทำสิ่งใหม่ต่อจากสิ่งที่ทำอยู่แล้ว'),('ทบทวนเบา ๆ','ปรับระบบให้เข้ากับชีวิตจริงทุกสัปดาห์')],ideas=['เป้าหมายบอกทิศทาง ระบบพาเราเดิน','เล็กแต่ทำซ้ำ ชนะใหญ่แต่เริ่มยาก','ระบบที่ดีต้องให้อภัยวันที่ไม่พร้อม']),
dict(slug='coffee-and-rain',title='กาแฟหนึ่งแก้วกับฤดูฝน',subtitle='เรื่องสั้นสำหรับวันที่ใจต้องการที่พัก',accent='#D18B57',premise='ก่อนร้านปิดในคืนฝนตก คนแปลกหน้าสองคนเลือกโต๊ะคนละมุม บทสนทนาสั้น ๆ ระหว่างเสียงฝนทำให้ทั้งคู่เห็นว่าการเริ่มใหม่ไม่จำเป็นต้องรอให้ฟ้าเปิด',beats=[('หลบฝน','ทั้งคู่เข้าร้านด้วยเรื่องที่ยังตัดสินใจไม่ได้'),('แก้วอุ่น','คำถามธรรมดาเปิดพื้นที่ให้เล่าอย่างซื่อตรง'),('ก้าวแรก','ฝนยังตก แต่ประตูร้านเปิดสู่ทางกลับบ้าน')],ideas=['การพักไม่ใช่การถอยหลัง','คนแปลกหน้าอาจคืนมุมมองที่เราทำหล่นไว้','ความกล้ามักเริ่มจากก้าวเล็ก ๆ ในวันที่ยังไม่พร้อม'])]

def build_fiction(d):
    out=OUT/(d['slug']+'.pdf');c=canvas.Canvas(str(out),pagesize=(W,H));art=ART/(d['slug']+'.png');total=4
    cover(c,d['title'],d['subtitle'],art,d['accent'],total)
    header(c,'01 • STORY','โลกของเรื่อง',d['accent']);rounded(c,44,72,400,340,'#FFFFFF','#E2DEF2',20);text(c,d['premise'],76,360,335,18,'#312E48','ThaiB',29,9);rounded(c,480,72,436,340,'#EEEAF8');image_fit(c,art,490,82,416,320);footer(c,2,total);c.showPage()
    header(c,'02 • THREE BEATS','สามจังหวะของเรื่อง',d['accent']);
    for i,(name,desc) in enumerate(d['beats']):
        x=55+i*300;rounded(c,x,155,270,235,'#FFFFFF','#E2DEF2',20);c.setFillColor(hx(d['accent']));c.circle(x+40,340,20,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('ThaiB',12);c.drawCentredString(x+40,336,str(i+1));text(c,name,x+25,292,220,19,'#2C2940','ThaiB',26,2);text(c,desc,x+25,235,220,13,'#625E73','Thai',21,5)
    footer(c,3,total);c.showPage()
    header(c,'03 • REFLECTION','สิ่งที่อยากชวนคิด',d['accent']);rounded(c,44,90,872,320,'#24233B')
    y=350
    for idea in d['ideas']:
        c.setFillColor(hx(d['accent']));c.circle(82,y+1,8,fill=1,stroke=0);y=text(c,idea,110,y+10,750,17,'#FFFFFF','ThaiB',27,3)-28
    text(c,'ลองเลือกหนึ่งประโยค แล้วเขียนต่ออีกสามบรรทัดจากประสบการณ์ของคุณ',110,128,740,12,'#D8D4E8','Thai',19,3);footer(c,4,total,True);c.save()

for d in technical:build_technical(d)
for d in fiction:build_fiction(d)
counts={p.stem:len(PdfReader(str(p)).pages) for p in OUT.glob('*.pdf')};(OUT/'manifest.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(counts,ensure_ascii=False))
