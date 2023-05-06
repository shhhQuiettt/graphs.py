from typing import Any
from graphs import Graph
from enum import Enum
from collections import deque


class SortType(Enum):
    KAHN = 1
    DFS = 2


def topological_sort(graph: Graph, algorithm: SortType):
    match algorithm:
        case SortType.DFS:
            return dfs_sort(graph)
        case SortType.KAHN:
            return kahn_sort(graph)


# Should return list?
def kahn_sort(graph: Graph) -> deque:
    return deque()


# Should return list?
def dfs_sort(graph: Graph) -> deque:
    ordered_verticies = deque()
    white = set()
    gray = set()
    black = set()

    def dfs_visit(graph: Graph, vertex: Any):
        gray.add(vertex)
        for neighbour in graph.vertex_neigbour_iterator(vertex):
            if neighbour in white:
                dfs_visit(graph, neighbour)

        # unneccessary line
        black.add(vertex)
        ordered_verticies.appendleft(vertex)

    for vertex in graph.vertices_iterator():
        white.add(vertex)

    for vertex in graph.vertices_iterator():
        if vertex in white:
            dfs_visit(graph, vertex)

    return ordered_verticies
