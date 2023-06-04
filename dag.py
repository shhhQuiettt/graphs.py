import graphs
import random, time

def make_dag(g: graphs.Graph, saturation: float, order: int, seed=1024):
    random.seed(seed)

    for _ in range(order):
        g.add_vertex()

    for i in range(order):
        for j in range(i + 1, order):
            if random.random() < saturation:
                g.add_edge(i, j)

    return g


# make_dag(graphs.DirectedIncidenceMatrix(0), 0.1, 10).print()

def dfs(graph,vertex, visit,wynik):

    visit[vertex] = True
    wynik+=1

    for successor in graph.vertex_neigbour_iterator(vertex):
        if visit[successor] == False:
            dfs(graph,vertex,visit,wynik)

    
    return wynik




def make_undirected_hc(g: graphs.Graph, density: float, order: int, seed=1024):
    random.seed(seed)

    for _ in range(order):
        g.add_vertex()

    # create a cycle
    for i in range(order-1):
        g.add_edge(i,i+1)
        g.add_edge(i+1,i)
    g.add_edge(order-1,0)
    g.add_edge(0,order-1)


    for i in range(order):
        for j in range(order):
            if i != j:
                if random.random() < density:
                    g.add_edge(i, j)
                    g.add_edge(j, i)

    return g

def make_undirected_ec(g: graphs.DirectedAdjacencyList, density: float, order: int, seed=1024):
    random.seed(seed)

    for _ in range(order):
        g.add_vertex()

    # create random grpah
    for i in range(order):
        for j in range(order):
            if i != j:
                if random.random() < density:
                    if j not in g.adj_list[i]:
                        g.add_edge(i, j)
                        g.add_edge(j, i)


    tab = []
    for i in range(order):
        if g.in_degree(i) %2 != 0:
            tab.append(i)


    for i in range(0,len(tab),2):
        if tab[i] in g.adj_list[tab[i+1]]:
            g.adj_list[tab[i+1]].remove(tab[i])
            g.adj_list[tab[i]].remove(tab[i+1])
        else:
            g.add_edge(tab[i], tab[i+1])
            g.add_edge(tab[i+1], tab[i])


    return g

    
p = make_undirected_ec(graphs.DirectedAdjacencyList(0),0.30,5, time.time())


# print(random.random())

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
