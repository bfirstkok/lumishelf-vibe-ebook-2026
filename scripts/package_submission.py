from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
out=root/'ส่งอาจารย์'; out.mkdir(exist_ok=True)
readme=out/'README-ส่งอาจารย์.txt'
readme.write_text('''LumiShelf - ชุดส่งใบงาน Vibe Coding E-book 2026

ลิงก์โปรแกรม: https://vibecode-gamma-murex.vercel.app
ลิงก์ไฟล์งาน: https://github.com/bfirstkok/lumishelf-vibe-ebook-2026

Android:
- LumiShelf.apk = ไฟล์ติดตั้ง
- LumiShelf.aia = ไฟล์แก้ไขใน MIT App Inventor

หมายเหตุ: การชำระเงินและการส่งอีเมลเป็น DEMO ONLY ไม่มีการรับเงินจริงหรือส่งอีเมลจริง
อ่านรายงานและ SUBMISSION_CHECKLIST ก่อนส่ง
''',encoding='utf-8-sig')

target=out/'LumiShelf-Complete-Submission.zip'
include_dirs=['app','lib','public','supabase','tests']
include_files=['README.md','package.json','package-lock.json','tsconfig.json','next.config.ts','eslint.config.mjs','.env.example']
with ZipFile(target,'w',ZIP_DEFLATED) as z:
    z.write(readme,'README-ส่งอาจารย์.txt')
    z.write(root/'docs'/'VibeCoding_EbookShop_Report.pdf','รายงาน/VibeCoding_EbookShop_Report.pdf')
    z.write(root/'docs'/'SUBMISSION_CHECKLIST.md','รายงาน/SUBMISSION_CHECKLIST.md')
    z.write(root/'docs'/'production-test-results.json','รายงาน/production-test-results.json')
    for image in ['01-home.png','02-book-detail.png','03-checkout.png']:
        z.write(root/'docs'/image,'รายงาน/screenshots/'+image)
    z.write(root/'mobile'/'LumiShelf.apk','Android/LumiShelf.apk')
    z.write(root/'mobile'/'LumiShelf.aia','Android/LumiShelf.aia')
    for pdf in (root/'private'/'ebooks').glob('*.pdf'):
        z.write(pdf,'Ebooks/'+pdf.name)
    for d in include_dirs:
        for p in (root/d).rglob('*'):
            if p.is_file(): z.write(p,'Source/'+p.relative_to(root).as_posix())
    for f in include_files: z.write(root/f,'Source/'+f)
print(target, target.stat().st_size)
