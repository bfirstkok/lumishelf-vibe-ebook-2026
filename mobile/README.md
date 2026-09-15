# LumiShelf Mobile Wrapper

แอปมือถือใช้ MIT App Inventor `WebViewer` เปิดเว็บ Production URL ตามใบงาน

การตั้งค่าที่ต้องตรวจสอบก่อน Build:

- `HomeUrl`: `https://vibecode-gamma-murex.vercel.app`
- `FollowLinks`: true
- `IgnoreSslErrors`: false
- `UsesLocation`: false
- ปุ่ม Back: ถ้า WebViewer ย้อนกลับได้ให้ `GoBack` มิฉะนั้นปิดหน้าจอ

เปิดไฟล์ `.aia` ใน MIT App Inventor แล้วเลือก **Build → Android App (.apk)** เพื่อรับไฟล์ APK ที่ลงนามโดยระบบ App Inventor
