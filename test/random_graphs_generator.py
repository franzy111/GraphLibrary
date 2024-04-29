from GraphLibrary import Graph, Edge
from random import randint, shuffle


def get_chain(n: int, has_negative_weights: bool = False) -> Graph:
    graph = Graph()
    for i in range(n - 1):
        if has_negative_weights:
            graph.add_edge(Edge(i, i + 1, randint(-100_000, 100_000)))
        else:
            graph.add_edge(Edge(i, i + 1, randint(0, 200_000)))

    return graph


def get_tree(n: int, has_negative_weights: bool = False) -> Graph:
    graph = Graph()
    vertexes = [i for i in range(n)]
    shuffle(vertexes)
    for i in range(1, n):
        if has_negative_weights:
            if has_negative_weights:
                graph.add_edge(Edge(vertexes[randint(0, i - 1)], vertexes[i], randint(-100_000, 100_000)))
            else:
                graph.add_edge(Edge(vertexes[randint(0, i - 1)], vertexes[i], randint(0, 200_000)))
    return graph


def get_connected_graph(n: int, has_negative_weights: bool = False) -> Graph:
    graph = get_tree(n, has_negative_weights)
    unic_edges = set()
    for i in range(randint(0, min(100_000, n * (n - 1) // 2))):
        if has_negative_weights:
            unic_edges.add((randint(0, n - 1), randint(0, n - 1), randint(-100_000, 100_000)))
        else:
            unic_edges.add((randint(0, n - 1), randint(0, n - 1), randint(0, 200_000)))
    for edge in unic_edges:
        if not graph.has_edge(edge[0], edge[1]):
            graph.add_edge(Edge(edge[0], edge[1], edge[2]))
    return graph
