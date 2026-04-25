import time
from db import collection, alerts_collection
from email_alert import send_email_alert

last_alert = None

while True:
    data = list(collection.find().sort("_id", -1).limit(5))

    if len(data) < 5:
        time.sleep(5)
        continue

    mem = [d["memory"] for d in data]

    # 🔥 Aging Detection
    if mem[0] > mem[1] > mem[2] > mem[3] > mem[4]:
        if last_alert != "trend":
            print("⚠ Aging Detected")
            send_email_alert("Memory increasing continuously!")
            
            alerts_collection.insert_one({
                "message": "Aging detected",
                "time": time.strftime("%H:%M:%S")
            })
            last_alert = "trend"

    # 🔥 High Memory
    elif mem[0] > 80:
        if last_alert != "memory":
            print("⚠ High Memory")
            send_email_alert("Memory too high!")

            alerts_collection.insert_one({
                "message": "High memory",
                "time": time.strftime("%H:%M:%S")
            })
            last_alert = "memory"

    time.sleep(5)