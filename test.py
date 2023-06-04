import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import graphs
import dag
import timeit
import copy
import ec
import hc
import time
import random

order_ec = [10, 50, 70]

results_ec = {
    "10": [],
    "50": [],
    "70": [],
}

sys.setrecursionlimit(20000)

number = 20

density = [0.3, 0.5, 0.7]


for ord in order_ec:
    for dens in density:
        g = dag.make_undirected_ec(
            graphs.DirectedAdjacencyList(0), dens, ord, time.time())

        results_ec[str(ord)].append(
            timeit.timeit("ec.detect_ec(g)", globals=globals(), number=number)
        )

print(results_ec)


x = np.arange(len(density))
width = 0.15
multiplier = 0.1

fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in results_ec:
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     multiplier += 1

offset = width * multiplier
ax.bar(x+offset, results_ec["10"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_ec["50"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_ec["70"], width)
# multiplier += 1


ax.set_ylabel('Time [s]')
ax.set_title('detect Eulerian Cycle in graph with EC')
ax.set_xticks(x + width, [f"{s*100}%" for s in density])
ax.legend(loc='upper left', ncols=3)
plt.show()



print("co tam")

order_hc = [5, 10, 12, 14]

results_hc = {
    "5": [],
    "10": [],
    "12": [],
    "14": [],
}
print("elo")
for ord in order_hc:
    for dens in density:
        g = dag.generateGraphWithHC(ord, dens)

        results_hc[str(ord)].append(
            timeit.timeit("hc.robertsFlores(g)",
                          globals=globals(), number=number)
        )


x = np.arange(len(density))
width = 0.15
multiplier = 0.1

fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in results_ec:
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     multiplier += 1

offset = width * multiplier
ax.bar(x+offset, results_hc["5"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_hc["10"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_hc["12"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_hc["14"], width)
multiplier += 1


ax.set_ylabel('Time [s]')
ax.set_title('detect hamiltonian Cycle in graph with HC')
ax.set_xticks(x + width, [f"{s*100}%" for s in density])
ax.legend(loc='upper left', ncols=3)
plt.show()


results_nhc = {
    "5": [],
    "10": [],
    "12": [],
    "14": [],
}

for ord in order_hc:
    for dens in density:
        g = dag.generateGraphWithHC_elo(ord, dens)

        results_nhc[str(ord)].append(
            timeit.timeit("hc.robertsFlores(g)",
                          globals=globals(), number=number)
        )


x = np.arange(len(density))
width = 0.15
multiplier = 0.1

fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in results_ec:
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     multiplier += 1

offset = width * multiplier
ax.bar(x+offset, results_nhc["5"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_nhc["10"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_nhc["12"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_nhc["14"], width)
multiplier += 1


ax.set_ylabel('Time [s]')
ax.set_title('detect hamiltonian Cycle in graph without HC')
ax.set_xticks(x + width, [f"{s*100}%" for s in density])
ax.legend(loc='upper left', ncols=3)
plt.show()
