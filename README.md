# Sip & Still — Coffee Shop Website

เว็บไซต์ร้านกาแฟมินิมอล สร้างด้วย Python Flask

## ฟีเจอร์
- หน้าแรก (Hero) พร้อมข้อมูลร้าน
- เมนูเครื่องดื่มและอาหาร (3 หมวด)
- ระบบจองโต๊ะออนไลน์ (บันทึกลงไฟล์ JSON)
- ข้อมูลติดต่อและโซเชียลมีเดีย

## วิธีรัน

```bash
# 1. ติดตั้ง dependencies
pip install -r requirements.txt

# 2. รันเซิร์ฟเวอร์
python app.py

# 3. เปิดเบราว์เซอร์ไปที่
http://localhost:5000
```

## โครงสร้างไฟล์
```
coffee_shop/
├── app.py              # Flask backend
├── requirements.txt    # Python packages
├── reservations.json   # ข้อมูลการจอง (สร้างอัตโนมัติ)
└── templates/
    └── index.html      # หน้าเว็บหลัก
```

## ปรับแต่ง
- แก้ชื่อร้าน: หาคำว่า "Sip & Still" ใน index.html และ app.py
- แก้เมนู: แก้ตัวแปร `MENU` ใน app.py
- แก้ที่อยู่/เบอร์โทร: หาในส่วน `#contact` ใน index.html
- แก้เวลาเปิด: แก้ตรงส่วน hero-hours และ contact-block
