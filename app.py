from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

RESERVATIONS_FILE = "reservations.json"

def load_reservations():
    if os.path.exists(RESERVATIONS_FILE):
        with open(RESERVATIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_reservations(data):
    with open(RESERVATIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

MENU = {
    "coffee": [
        {"name": "Espresso", "price": 60, "desc": "กาแฟเข้มข้น ดื่มด่ำทุกซิป"},
        {"name": "Americano", "price": 65, "desc": "เอสเพรสโซ่ผสมน้ำร้อน กลมกล่อม"},
        {"name": "Latte", "price": 80, "desc": "เอสเพรสโซ่กับนมสด ครีมมี่"},
        {"name": "Cappuccino", "price": 80, "desc": "โฟมนมหนานุ่ม คลาสสิค"},
        {"name": "Cold Brew", "price": 90, "desc": "ชงเย็น 12 ชั่วโมง หวานธรรมชาติ"},
        {"name": "Signature Honey Latte", "price": 95, "desc": "ลาเต้น้ำผึ้งแท้ เมนูแนะนำ"},
    ],
    "non_coffee": [
        {"name": "Matcha Latte", "price": 85, "desc": "มัทฉะแท้จากญี่ปุ่น"},
        {"name": "Hojicha", "price": 85, "desc": "ชาเขียวคั่ว กลิ่นหอมนุ่ม"},
        {"name": "Chocolate", "price": 80, "desc": "ช็อคโกแลตร้อน-เย็น เข้มข้น"},
        {"name": "Lemonade", "price": 70, "desc": "มะนาวสด เปรี้ยวหวานสดชื่น"},
    ],
    "food": [
        {"name": "Croissant", "price": 55, "desc": "เนยแท้ อบสดทุกเช้า"},
        {"name": "Banana Bread", "price": 60, "desc": "กล้วยหอมทองคู่กาแฟได้ดี"},
        {"name": "Avocado Toast", "price": 120, "desc": "อะโวคาโดสดบนขนมปังโฮลวีต"},
        {"name": "Egg Sandwich", "price": 95, "desc": "ไข่ดาวชีส อิ่มเริ่มเช้า"},
    ]
}

@app.route("/")
def index():
    return render_template("index.html", menu=MENU)

@app.route("/api/reserve", methods=["POST"])
def reserve():
    data = request.get_json()
    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    date = data.get("date", "").strip()
    time = data.get("time", "").strip()
    guests = data.get("guests", 1)
    note = data.get("note", "").strip()

    if not all([name, phone, date, time]):
        return jsonify({"success": False, "message": "กรุณากรอกข้อมูลให้ครบถ้วน"}), 400

    reservations = load_reservations()
    reservation = {
        "id": len(reservations) + 1,
        "name": name,
        "phone": phone,
        "date": date,
        "time": time,
        "guests": guests,
        "note": note,
        "created_at": datetime.now().isoformat()
    }
    reservations.append(reservation)
    save_reservations(reservations)

    return jsonify({"success": True, "message": f"จองโต๊ะสำเร็จ! เราจะรอต้อนรับคุณ {name} ในวันที่ {date} เวลา {time} น."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
