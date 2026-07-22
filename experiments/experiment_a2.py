import matplotlib.pyplot as plt

servers = [2, 3, 4, 5, 6]
average_load = [5000, 3333, 2500, 2000, 1667]

plt.plot(servers, average_load, marker="o")

plt.title("Average Load vs Number of Servers")
plt.xlabel("Number of Servers")
plt.ylabel("Average Requests per Server")

plt.savefig("A2_line_chart.png")
plt.show()