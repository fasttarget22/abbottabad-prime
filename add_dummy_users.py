import urllib.request
import json
from datetime import datetime, timedelta

API_KEY = "AIzaSyD37yFDGpB8bLQDLzPcyih65os63p6_6v0"
PROJECT = "abbottabad-prime"
BASE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT}/databases/(default)/documents/vendors"

now = datetime.utcnow().isoformat() + "Z"
trial = (datetime.utcnow() + timedelta(days=60)).isoformat() + "Z"

users = [
    {"name":"Dr. Ahmed Khan","email":"doctor@test.com","password":"test123","category":"General Physician","city":"Abbottabad","phone":"03001111111","experience":"10","fee":"500","hours":"9AM-5PM","description":"General physician with 10 years experience","address":"Main Bazaar Abbottabad"},
    {"name":"Ali Khan","email":"patient@test.com","password":"test123","category":"Patient","city":"Abbottabad","phone":"03002222222","experience":"0","fee":"0","hours":"N/A","description":"Test patient","address":"Civil Lines Abbottabad"},
    {"name":"City Lab","email":"lab@test.com","password":"test123","category":"Laboratory","city":"Abbottabad","phone":"03003333333","experience":"5","fee":"200","hours":"8AM-8PM","description":"Full diagnostic lab services","address":"Jinnah Road Abbottabad"},
    {"name":"Prime Pharma","email":"pharmacy@test.com","password":"test123","category":"Pharmacy","city":"Abbottabad","phone":"03004444444","experience":"8","fee":"0","hours":"24 Hours","description":"All medicines available","address":"Hospital Road Abbottabad"},
    {"name":"Fast Rides","email":"transport@test.com","password":"test123","category":"Transport","city":"Abbottabad","phone":"03005555555","experience":"3","fee":"100","hours":"24 Hours","description":"Fast and reliable transport","address":"Mansehra Road Abbottabad"},
    {"name":"Scan Center","email":"diagnostics@test.com","password":"test123","category":"Diagnostics","city":"Abbottabad","phone":"03006666666","experience":"7","fee":"1000","hours":"9AM-6PM","description":"MRI, Xray, Ultrasound","address":"Shimla Hill Abbottabad"},
    {"name":"Dr. Sara Ali","email":"doctor2@test.com","password":"test123","category":"Eye Specialist","city":"Lahore","phone":"03007777777","experience":"15","fee":"800","hours":"10AM-4PM","description":"Eye specialist with 15 years experience","address":"Gulberg Lahore"},
    {"name":"HealthCare Pharmacy","email":"pharmacy2@test.com","password":"test123","category":"Pharmacy","city":"Lahore","phone":"03008888888","experience":"10","fee":"0","hours":"8AM-10PM","description":"Quality medicines at best prices","address":"DHA Lahore"},
]

def add_user(user):
    data = {
        "fields": {
            "name": {"stringValue": user["name"]},
            "email": {"stringValue": user["email"]},
            "password": {"stringValue": user["password"]},
            "category": {"stringValue": user["category"]},
            "city": {"stringValue": user["city"]},
            "phone": {"stringValue": user["phone"]},
            "experience": {"stringValue": user["experience"]},
            "fee": {"stringValue": user["fee"]},
            "hours": {"stringValue": user["hours"]},
            "description": {"stringValue": user["description"]},
            "address": {"stringValue": user["address"]},
            "status": {"stringValue": "online"},
            "adminApproved": {"booleanValue": True},
            "verified": {"booleanValue": True},
            "suspended": {"booleanValue": False},
            "rating": {"stringValue": "5.0"},
            "votes": {"stringValue": "0"},
            "photo": {"stringValue": ""},
            "cnic": {"stringValue": ""},
            "lat": {"stringValue": ""},
            "lng": {"stringValue": ""},
            "subscription": {"stringValue": "trial"},
            "registered": {"stringValue": now},
            "approvedAt": {"stringValue": now},
            "trialEnd": {"stringValue": trial},
        }
    }
    body = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{BASE_URL}?key={API_KEY}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        res = urllib.request.urlopen(req)
        print(f"✅ Added: {user['name']} ({user['email']})")
    except Exception as e:
        print(f"❌ Failed: {user['name']} — {e}")

for user in users:
    add_user(user)

print("\n✅ All dummy users created!")
