import matplotlib.pyplot as plt

servers = ["S1", "S2", "S3"]
counts = [3370, 3315, 3315]

plt.bar(servers, counts)

plt.title("Load Distribution for 10000 Requests")
plt.xlabel("Servers")
plt.ylabel("Requests")

plt.savefig("A1_bar_chart.png")

plt.show()