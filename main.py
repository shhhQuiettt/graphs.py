import dag
import graphs
import sorts

# g = radnom_dag_adjacency_matrix(6)
# g = graphs.DirectedAdjacencyMatrix.from_matrix(
#     [[0, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
# )
# g = DirectedAdjacencyList.from_list([[1, 3], [], [0], []])

# g = graphs.DirectedIncidenceMatrix.from_matrix(
#     [[1, -1, 1], [-1, 0, 0], [0, 1, 0], [0, 0, -1]]
# )


# g.print()

# print(sorts.topological_sort(g, sorts.SortType.DFS))
# print(sorts.topological_sort(g, sorts.SortType.KAHN))

# g = dag.random_dag_forward_star(6, 0.5)
g = dag.random_dag_incidence_matrix(4, 0.5)
g.print()

print(sorts.topological_sort(g, sorts.SortType.DFS))
print(sorts.topological_sort(g, sorts.SortType.KAHN))
