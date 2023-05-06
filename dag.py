import graphs
import random


def radnom_dag_adjacency_matrix(vertex_numer: int) -> graphs.DirectedAdjacencyMatrix:
    graph = graphs.DirectedAdjacencyMatrix(number_of_verticies=vertex_numer)
    for i in range(vertex_numer):
        for j in range(i + 1, vertex_numer):
            if i != j:
                if random.randint(0, 2) >= 1:
                    graph.add_edge(i, j)

    return graph


def random_dag_adjacency_list() -> graphs.DirectedAdjacencyList:
    return graphs.DirectedAdjacencyList(number_of_verticies=0)
