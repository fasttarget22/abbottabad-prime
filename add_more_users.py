import urllib.request
import json
from datetime import datetime, timedelta

API_KEY = "AIzaSyD37yFDGpB8bLQDLzPcyih65os63p6_6v0"
PROJECT = "abbottabad-prime"
BASE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT}/databases/(default)/documents/vendors"

now = datetime.now().isoformat() + "Z"
trial = (datetime.now() + timedelta(days=60)).isoformat() + "Z"

users = [
    {"name":"City Restaurant","email":"restaurant@test.com","password":"test123","category":"Restaurants & Food","city":"Abbottabad","phone":"03011111111","experience":"5","fee":"0","hours":"9AM-11PM","description":"Best food in Abbottabad","address":"Main Bazaar Abbottabad"},
    {"name":"Prime Store","email":"shop@test.com","password":"test123","category":"Shops & Stores","city":"Abbottabad","phone":"03022222222","experience":"3","fee":"0","hours":"9AM-9PM","description":"All household items available","address":"Jinnah Road Abbottabad"},
    {"name":"Tech Fix","email":"tech@test.com","password":"test123","category":"Technical & Home Services","city":"Abbottabad","phone":"03033333333","experience":"7","fee":"500","hours":"9AM-6PM","description":"All technical repairs","address":"Hospital Road Abbottabad"},
    {"name":"Glamour Salon","email":"beauty@test.com","password":"test123","category":"Beauty & Wellness","city":"Abbottabad","phone":"03044444444","experience":"4","fee":"300","hours":"10AM-8PM","description":"Best beauty salon","address":"Shimla Hill Abbottabad"},
    {"name":"Prime Properties","email":"property@test.com","password":"test123","category":"Property & Real Estate","city":"Abbottabad","phone":"03055555555","experience":"10","fee":"0","hours":"9AM-5PM","description":"Buy sell rent properties","address":"Civil Lines Abbottabad"},
    {"name":"Smart Tutors","email":"education@test.com","password":"test123","category":"Education & Tutors","city":"Abbottabad","phone":"03066666666","experience":"8","fee":"500","hours":"8AM-8PM","description":"Expert tutors for all subjects","address":"Mansehra Road Abbottabad"},
    {"name":"Click Photography","email":"events@test.com","password":"test123","category":"Events & Photography","city":"Abbottabad","phone":"03077777777","experience":"6","fee":"5000","hours":"9AM-9PM","description":"Professional photography","address":"Abbottabad"},
    {"name":"Digital Solutions","email":"it@test.com","password":"test123","category":"IT & Digital Services","city":"Abbottabad","phone":"03088888888","experience":"5","fee":"1000","hours":"9AM-6PM","description":"Web design, SEO, IT solutions","address":"Abbottabad"},
    {"name":"City Car Rental","email":"carshare@test.com","password":"test123","category":"Car Share & Intercity","city":"Abbottabad","phone":"03099999999","experience":"4","fee":"2000","hours":"24 Hours","description":"Intercity car service","address":"Abbottabad"},
    {"name":"Speedy Bikes","email":"bike@test.com","password":"test123","category":"Bike & Local Transport","city":"Abbottabad","phone":"03010101010","experience":"2","fee":"100","hours":"8AM-10PM","description":"Fast bike delivery service","address":"Abbottabad"},
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

print("\n✅ All users created!")
