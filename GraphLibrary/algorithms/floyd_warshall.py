from GraphLibrary.structure.Graph import Graph


def floyd_warshall(n: int, graph: Graph, start: int, finish: int) -> list:
    """
    Выполняет алгоритм Флойда-Уоршелла для нахождения кратчайших путей между всеми парами вершин в графе.

    :param n: (int): Количество вершин в графе.
    :param graph: (Graph): Граф, для которого нужно найти кратчайшие пути.
    :param start: (int): Индекс начальной вершины.
    :param finish: (int): Индекс конечной вершины.

    :return: Список, представляющий кратчайший путь от начальной до конечной вершины.
    """
    graph = graph.to_adjacency_matrix()
    next_vertex = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j]:
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    return _get_path(next_vertex, start, finish)


def _get_path(next_vertex, start, end):
    path = [start]
    while start != end:
        start = next_vertex[start][end]
        path.append(start)
    return path
