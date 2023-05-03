from graphs import Graph
from enum import Enum


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
def kahn_sort(graph: Graph) -> list:
    return list()


# Should return list?
def dfs_sort(graph: Graph) -> list:
    return list()
