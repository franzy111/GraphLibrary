from GraphLibrary.structure.Graph import Graph


def floyd_warshall(n: int, graph: Graph, start: int, finish: int) -> list:
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
    return get_path(next_vertex, start, finish)


def get_path(next_vertex, start, end):
    path = [start]
    while start != end:
        start = next_vertex[start][end]
        path.append(start)
    return path
