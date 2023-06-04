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

sys.setrecursionlimit(20000)

number = 20

order_ec = [10,50,70]
density = [0.3, 0.5, 0.7]

results_nec = {
    "10": [],
    "50": [],
    "70": [],
}


for ord in order_ec:
    for dens in density:
        g = dag.make_undirected_nec(graphs.DirectedAdjacencyList(0),dens,ord,time.time())

        results_nec[str(ord)].append(
            timeit.timeit("ec.detect_ec(g)", globals=globals(), number=number)
        )

print("ok")
x = np.arange(len(density))
width = 0.15
multiplier = 0.1

fig, ax = plt.subplots(layout='constrained')


offset = width * multiplier
ax.bar(x+offset, results_nec["10"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_nec["50"], width)
multiplier += 1
offset = width * multiplier
ax.bar(x+offset, results_nec["70"], width)
# multiplier += 1


ax.set_ylabel('Time [s]')
ax.set_title('detect Eulerian Cycle in graph without EC')
ax.set_xticks(x + width, [f"{s*100}%" for s in density])
ax.legend(loc='upper left', ncols=3)
plt.show()
