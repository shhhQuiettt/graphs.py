from collections import defaultdict
import graphs

def Hamiltonian(graph, v, visited, path, start):
    visited[v] = True
    path.append(v)

    if len(path) == graph.number_of_verticies and start in graph.adj_list[path[-1]] and path[-1]!= path[1]:
        return True

    for successor in graph.vertex_neigbour_iterator(v):
        if not visited[successor]:
            if Hamiltonian(graph, successor, visited, path, start):
                return True

    visited[v] = False
    path.pop()
    return False

def flores(graph):
    visited = [ False for v in graph.vertices_iterator()]
    cycle = []
    start = 0

    if Hamiltonian(graph, start, visited, cycle, start):
        cycle.append(start)
        return cycle

    print("not found")
    return False


def robertsFlores(graph):
    path = []
    nodes = graph.number_of_verticies
    startNode = 0
    path.append(startNode)
    numberOfVisitedChilds = defaultdict(lambda: 0)

    while(path):
        actualNode = path[-1]
        if numberOfVisitedChilds[actualNode] == len(graph.adj_list[actualNode]):
            path.pop(-1)
            numberOfVisitedChilds[actualNode] = 0
            continue
        if len(path) == nodes:
            if startNode in graph.adj_list[path[-1]]:
                # print(f"Path: {path}")
                # print("Found Hamiltonial Cycle")
                return True
        if graph.adj_list[actualNode][numberOfVisitedChilds[actualNode]] not in path:
            path.append(graph.adj_list[actualNode][numberOfVisitedChilds[actualNode]])
        numberOfVisitedChilds[actualNode] += 1
    print("Not found Hamiltonial Cycle")
    return False