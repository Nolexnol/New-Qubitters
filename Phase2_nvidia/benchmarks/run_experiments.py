import cudaq
cudaq.set_target("nvidia")  
import time
import json
from Phase2_nvidia.pipeline import run_quantum_seeded_mts

Ns = [10, 12, 16, 24, 30]
results = []

for n in Ns:
    start = time.time()
    seq, energy = run_quantum_seeded_mts(
        n=n,
        shots=300,
        max_iters=1000
    )
    elapsed = time.time() - start
    results.append({
        "N": n,
        "energy": energy,
        "time": elapsed
    })
    print(f"N={n}, Energy={energy}, Time={elapsed:.2f}s")

with open("results_gpu.json", "w") as f:
    json.dump(results, f, indent=2)
