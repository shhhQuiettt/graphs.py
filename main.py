import dag
from graphs import DirectedAdjacencyMatrix, DirectedAdjacencyList
import sorts

# g = radnom_dag_adjacency_matrix(6)
# g = DirectedAdjacencyMatrix.from_matrix(
#     [[0, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
# )
# g = DirectedAdjacencyList.from_list([[1, 3], [], [0], []])

g = dag.random_dag_adjacency_list(6, 0.5)

g.print()

# print(sorts.topological_sort(g, sorts.SortType.DFS))
