from typing import Any
import graphs


def detect_ec(graph: graphs.DirectedAdjacencyList):
    ordered_verticies = []

    def dfs_visit(graph: graphs.Graph, vertex: Any, predecessor: Any):
        
        if vertex != predecessor:
            graph.remove_edge(vertex, predecessor)
            graph.remove_edge(predecessor,vertex)

        neighbour = graph.get_neighbour(vertex)
        if neighbour != -1:
            dfs_visit(graph, neighbour, vertex)

        ordered_verticies.append(vertex)


    dfs_visit(graph, 0, 0)

    return ordered_verticies
