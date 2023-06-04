import graphs

def Hamiltonian(graph, v, visited, path, start):
    visited[v] = True
    path.append(v)

    if len(path) == graph.number_of_verticies and start in graph.vertex_neigbour_iterator(v):
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

    return False


