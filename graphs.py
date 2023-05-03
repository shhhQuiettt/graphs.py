from abc import ABC, abstractmethod


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


class DirectedAdjacencyMatrix(Graph):
    def __init__(self, number_of_verticies: int):
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
