from structure.Graph import Graph


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
    path = [start + 1]
    while start != end:
        start = next_vertex[start][end]
        path.append(1 + start)
    return path


'''
def main():
    # Граф задаётся матрицей смежности, где m[a][b] = weight, если между ними есть путь
    # Тут удобнее в 0-индексации
    n = int(input())
    start, finish = map(int, input().split())
    start -= 1
    finish -= 1
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            graph[i][j] = temp[j]
    ans, for_path = floyd_warshall(n, graph)
    if ans[start][finish] != float('inf'):
        return ans[start][finish], get_path(for_path, start, finish)
    else:
        return -1


if __name__ == '__main__':
    print(main())
'''
