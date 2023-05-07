from typing import Any
from graphs import Graph
from enum import Enum
from collections import deque


class SortType(Enum):
    KAHN = 1
    DFS = 2


def topological_sort(graph: Graph, algorithm: SortType) -> deque:
    match algorithm:
        case SortType.DFS:
            return dfs_sort(graph)
        case SortType.KAHN:
            return kahn_sort(graph)


def kahn_sort(graph: Graph) -> deque:
    ordered_verticies = deque()
    que = deque()
    in_degrees = {}

    for vertex in graph.vertices_iterator():
        curr_in_degree = graph.in_degree(vertex)
        in_degrees[vertex] = curr_in_degree

        if curr_in_degree == 0:
            que.append(vertex)
            ordered_verticies.append(vertex)

    while len(que) > 0:
        vertex = que.pop()
        for neighbour_vertex in graph.vertex_neigbour_iterator(vertex):
            in_degrees[neighbour_vertex] -= 1
            if in_degrees[neighbour_vertex] == 0:
                que.append(neighbour_vertex)
                ordered_verticies.append(neighbour_vertex)

    return ordered_verticies


def dfs_sort(graph: Graph) -> deque:
    ordered_verticies = deque()
    white = set()
    gray = set()
    black = set()

    def dfs_visit(graph: Graph, vertex: Any):
        white.remove(vertex)
        gray.add(vertex)
        for neighbour in graph.vertex_neigbour_iterator(vertex):
            if neighbour in white:
                dfs_visit(graph, neighbour)

        # unneccessary line
        gray.remove(vertex)
        black.add(vertex)
        ordered_verticies.appendleft(vertex)

    for vertex in graph.vertices_iterator():
        white.add(vertex)

    for vertex in graph.vertices_iterator():
        if vertex in white:
            dfs_visit(graph, vertex)

    return ordered_verticies
