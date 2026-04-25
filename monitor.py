import psutil
import time
from db import collection

email = "user@gmail.com"

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    data = {
        "email": email,
        "cpu": cpu,
        "memory": memory,
        "time": time.strftime("%H:%M:%S")
    }

    collection.insert_one(data)
    print("Saved:", data)

    time.sleep(5)
