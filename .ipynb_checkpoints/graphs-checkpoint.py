from abc import ABC, abstractmethod
from collections.abc import Iterable
import enum
from typing import Generator, Any


class Graph(ABC):
    @abstractmethod
    def add_vertex(self, v):
        pass

    @abstractmethod
    def remove_vertex(self, v):
        pass

    @abstractmethod
    def add_edge(self, v1, v2):
        pass

    @abstractmethod
    def remove_edge(self, v1, v2):
        pass

    @abstractmethod
    def vertices_iterator(self) -> Generator:
        pass

    @abstractmethod
    def vertex_neigbour_iterator(self, v: Any) -> Generator:
        pass

    @abstractmethod
    def in_degree(self, v: Any) -> int:
        pass

    @abstractmethod
    def print(self):
        pass


class DirectedAdjacencyMatrix(Graph):
    def __init__(self, number_of_verticies: int):
        self.number_of_verticies = number_of_verticies
        self.matrix = [
            [0 for _ in range(number_of_verticies)] for _ in range(number_of_verticies)
        ]

    def add_vertex(self, v=None):
        if v is not None:
            raise NotImplementedError("AdjecencyMatrix does not support vertex labels")

        self.matrix.append([0 for _ in range(len(self.matrix))])
        for row in self.matrix:
            row.append(0)

    def remove_vertex(self, v):
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0

    def in_degree(self, v: Any) -> int:
        return sum([row[v] for row in self.matrix])

    def vertices_iterator(self):
        return range(len(self.matrix))

    def vertex_neigbour_iterator(self, v):
        for i in range(self.number_of_verticies):
            if self.matrix[v][i] == 1:
                yield i

    @classmethod
    def from_matrix(cls, m):
        graph = cls(len(m))
        graph.matrix = m
        return graph

    def print(self):
        for row in self.matrix:
            print(row)


class DirectedAdjacencyList(Graph):
    def __init__(self, number_of_verticies: int):
        self.adj_list = [[] for _ in range(number_of_verticies)]

    @classmethod
    def from_list(cls, adj_list: list):
        graph = cls(len(adj_list))
        graph.adj_list = adj_list
        return graph

    def add_vertex(self, v=None):
        if v is not None:
            raise NotImplementedError("AdjecencyList does not support vertex labels")

        self.adj_list.append([])

    def remove_vertex(self, v):
        self.adj_list.pop(v)

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)

    def remove_edge(self, v1, v2):
        self.adj_list[v1].remove(v2)

    def in_degree(self, v: Any) -> int:
        return sum([v in row for row in self.adj_list])

    def vertices_iterator(self):
        return range(len(self.adj_list))

    def vertex_neigbour_iterator(self, v):
        for i in range(len(self.adj_list[v])):
            yield self.adj_list[v][i]

    def print(self):
        for i, row in enumerate(self.adj_list):
            print(f"{i}: {row}")


class DirectedArcList(Graph):
    def __init__(self, number_of_verticies: int):
        self.arc_list = []
        self.number_of_verticies = number_of_verticies

    def add_vertex(self, v=None):
        raise NotImplementedError("ArcList does not support vertex adding")

    def remove_vertex(self, v):
        raise NotImplementedError("ArcList does not support vertex removal")

    def add_edge(self, v1, v2):
        self.arc_list.append((v1, v2))

    def remove_edge(self, v1, v2):
        self.arc_list.remove((v1, v2))

    def in_degree(self, v: Any) -> int:
        return sum([arc[1] == v for arc in self.arc_list])

    def vertices_iterator(self):
        return range(self.number_of_verticies)

    def vertex_neigbour_iterator(self, v):
        for arc in self.arc_list:
            if arc[0] == v:
                yield arc[1]

    def print(self):
        for arc in self.arc_list:
            print(f"{arc[0]} -> {arc[1]}")

    @classmethod
    def from_list(cls, arc_list: list):
        graph = cls(len(arc_list))
        graph.arc_list = arc_list
        return graph


class DirectedIncidenceMatrix(Graph):
    def __init__(self, number_of_verticies: int) -> None:
        self.number_of_verticies = number_of_verticies
        self.matrix = [[] for _ in range(number_of_verticies)]

    def add_vertex(self, v=None):
        if v is not None:
            raise NotImplementedError("IncidenceMatrix does not support vertex labels")

        self.matrix.append([])

    def remove_vertex(self, v):
        self.matrix.pop(v)

    def add_edge(self, v1, v2):
        for v_id, row in enumerate(self.matrix):
            if v_id != v1 and v_id != v2:
                row.append(0)
            else:
                row.append(1) if v_id == v1 else row.append(-1)

    def remove_edge(self, v1, v2):
        edge_id = -1
        for e_id in range(len(self.matrix[v1])):
            if self.matrix[e_id][v1] == 1 and self.matrix[e_id][v2] == -1:
                edge_id = e_id
                break
        for row in self.matrix:
            row.pop(edge_id)

    def in_degree(self, v: Any) -> int:
        d = 0
        for e_id in self.matrix[v]:
            if e_id == -1:
                d += 1
        return d

    def vertices_iterator(self):
        return range(len(self.matrix))

    def vertex_neigbour_iterator(self, v):
        for e_id, edge in enumerate(self.matrix[v]):
            if edge == 1:
                for v_id, row in enumerate(self.matrix):
                    if row[e_id] == -1:
                        yield v_id

    def print(self):
        for row in self.matrix:
            print(row)

    @classmethod
    def from_matrix(cls, m):
        graph = cls(len(m))
        graph.matrix = m
        return graph


class DirectedForwardStar(Graph):
    def __init__(self, number_of_verticies: int) -> None:
        self.number_of_verticies = number_of_verticies
        self.forward_star = []
        self.forward_star.append((0, 0))

    def add_vertex(self, v=None):
        pass

    def remove_vertex(self, v):
        raise NotImplementedError("ForwardStar does not support vertex removal")

    def add_edge(self, v1, v2):
        self.forward_star.append((v1, v2))

    def remove_edge(self, v1, v2):
        self.forward_star.remove((v1, v2))

    def in_degree(self, v: Any) -> int:
        return sum([arc[1] == v for arc in self.forward_star])

    def vertices_iterator(self):
        return range(self.number_of_verticies)

    def vertex_neigbour_iterator(self, v):
        for arc in self.forward_star:
            if arc[0] == v:
                yield arc[1]

    def print(self):
        for arc in self.forward_star:
            print(f"{arc[0]} -> {arc[1]}")

    @classmethod
    def from_list(cls, forward_star: list):
        graph = cls(len(forward_star))
        graph.forward_star = forward_star
        return graph
