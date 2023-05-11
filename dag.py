import graphs
import random


def make_dag(g: graphs.Graph, saturation: float, order: int, seed=1024):
    random.seed(seed)

    for _ in range(order):
        g.add_vertex()

    for i in range(order):
        for j in range(i + 1, order):
            if random.random() < saturation:
                g.add_edge(i, j)

    return g


make_dag(graphs.DirectedIncidenceMatrix(0), 0.1, 10).print()

# def radnom_dag_adjacency_matrix(
#     vertex_numer: int, density: float
# ) -> graphs.DirectedAdjacencyMatrix:
#     graph = graphs.DirectedAdjacencyMatrix(number_of_verticies=vertex_numer)
#     for i in range(vertex_numer):
#         for j in range(i + 1, vertex_numer):
#             if i != j:
#                 if random.random() < density:
#                     graph.add_edge(i, j)

#     return graph


# def random_dag_adjacency_list(
#     vertex_number: int, density: float
# ) -> graphs.DirectedAdjacencyList:
#     adj_list = [[] for i in range(vertex_number)]
#     for i in range(vertex_number):
#         for j in range(i + 1, vertex_number):
#             if random.random() < density:
#                 adj_list[i].append(j)
#     return graphs.DirectedAdjacencyList.from_list(adj_list)


# def random_dag_forward_star(
#     vertex_number: int, density: float
# ) -> graphs.DirectedForwardStar:
#     adj_list = [[] for i in range(vertex_number)]
#     for i in range(vertex_number):
#         for j in range(i + 1, vertex_number):
#             if random.random() < density:
#                 adj_list[i].append(j)
#     return graphs.DirectedForwardStar.from_list(adj_list)


# def random_dag_arc_list(vertex_number: int, density: float) -> graphs.DirectedArcList:
#     arc_list = []
#     for i in range(vertex_number):
#         for j in range(i + 1, vertex_number):
#             if random.random() < density:
#                 arc_list.append((i, j))
#     return graphs.DirectedArcList.from_list(arc_list, vertex_number)


# def random_dag_incidence_matrix(
#     num_vertices: int, density: float
# ) -> graphs.DirectedIncidenceMatrix:
#     adj_list_graph = random_dag_adjacency_list(num_vertices, density)

#     inc_matrix = graphs.adjacency_list_to_incidence_matrix(adj_list_graph.adj_list)

#     return graphs.DirectedIncidenceMatrix.from_matrix(inc_matrix, num_vertices)
