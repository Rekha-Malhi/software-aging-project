import matplotlib.pyplot as plt
from db import collection

data = list(collection.find())

cpu = [d["cpu"] for d in data]
memory = [d["memory"] for d in data]

plt.plot(cpu, label="CPU")
plt.plot(memory, label="Memory")

plt.xlabel("Time")
plt.ylabel("Usage %")
plt.title("System Monitoring Graph")

plt.legend()
plt.show()