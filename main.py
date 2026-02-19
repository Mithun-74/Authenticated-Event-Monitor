import requests
import json
import time
import os
from dotenv import load_dotenv

# ==================================
# LOAD ENV VARIABLES
# ==================================
load_dotenv()

COOKIE = os.getenv("COOKIE")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("🚀 Event Monitor Starting...")
print("COOKIE loaded:", "YES" if COOKIE else "NO")
print("BOT TOKEN loaded:", "YES" if BOT_TOKEN else "NO")
print("CHAT ID:", CHAT_ID)

URL = "https://bip.bitsathy.ac.in/nova-api/student-activity-masters?page=1"

HEADERS = {
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0"
}

# ==================================
# TELEGRAM NOTIFICATION
# ==================================
def notify(msg):
    try:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": msg}
        )
    except Exception as e:
        print("Telegram Error:", e)

# ==================================
# EXTRACT FIELDS
# ==================================
def extract_fields(fields):
    data = {}
    for f in fields:
        key = f.get("validationKey")
        value = f.get("value")
        data[key] = value
    return data

# ==================================
# FILTER RULES
# ==================================
def is_valid(event):
    return (
        event["status"] == "Active"
        and event["location"] == "ONLINE"
        and event["event_category"] in ["Competition", "Paper Presentation"]
    )

# ==================================
# LOAD SEEN IDS FROM FILE
# ==================================
if os.path.exists("seen.json"):
    with open("seen.json", "r") as f:
        seen = set(json.load(f))
else:
    seen = set()

# ==================================
# MAIN CHECK FUNCTION
# ==================================
def check_events():

    print("🔎 Checking events...")

    r = requests.get(URL, headers=HEADERS)

    print("Status code:", r.status_code)

    # SESSION EXPIRED ALERT
    if r.status_code != 200:
        print("⚠️ Session expired!")
        notify("⚠️ Session expired! Please refresh cookie.")
        return

    data = r.json()

    found_any = False

    for e in data["resources"]:
        title = e.get("title","")
        fields = extract_fields(e.get("fields",[]))

        event = {
            "title": title,
            "event_code": fields.get("event_code"),
            "event_category": fields.get("event_category"),
            "status": fields.get("status"),
            "location": fields.get("location")
        }

        event_id = event["event_code"]

        if not event_id:
            continue

        if is_valid(event) and event_id not in seen:

            message = (
                "🚨 NEW ONLINE EVENT FOUND\n\n"
                f"{title}"
            )

            print(message)
            notify(message)

            seen.add(event_id)
            found_any = True

    # Save seen IDs
    with open("seen.json", "w") as f:
        json.dump(list(seen), f)

    if not found_any:
        print("✅ No new matching events.")

# ==================================
# LOOP
# ==================================
print("🔄 Monitor Running... (Press CTRL+C to stop)\n")

while True:
    try:
        check_events()
        print("⏳ Waiting 60 seconds...\n")
    except Exception as e:
        print("Error:", e)

    time.sleep(60)
