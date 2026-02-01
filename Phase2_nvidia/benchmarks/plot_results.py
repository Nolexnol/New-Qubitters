import json
import matplotlib.pyplot as plt

with open("results_gpu.json") as f:
    data = json.load(f)

Ns = [d["N"] for d in data]
times = [d["time"] for d in data]
energies = [d["energy"] for d in data]

# Time vs N
plt.figure()
plt.plot(Ns, times, marker="o")
plt.xlabel("Sequence Length (N)")
plt.ylabel("Time to Solution (s)")
plt.title("GPU Time-to-Solution vs N")
plt.grid()
plt.savefig("time_vs_n.png")
plt.show()

# Energy vs N
plt.figure()
plt.plot(Ns, energies, marker="o")
plt.xlabel("Sequence Length (N)")
plt.ylabel("Best Energy Found")
plt.title("Solution Quality vs N")
plt.grid()
plt.savefig("energy_vs_n.png")
plt.show()
