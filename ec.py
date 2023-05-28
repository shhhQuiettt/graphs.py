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


    if ordered_verticies[0] != ordered_verticies[len(ordered_verticies) - 1]:
        return False 
    return True

tab = []
tab.append([1,2,3])
tab.append([2,0])
tab.append([1,0,3])
tab.append([2,0])


# print(tab[5][0])

g = graphs.DirectedAdjacencyList.from_list(tab)
g.print()

order = detect_ec(g)
print(order)