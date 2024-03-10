def floyd_warshall(n: int, graph: list) -> list:
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j]:
                dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


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
    ans = floyd_warshall(n, graph)
    if ans[start][finish] != float('inf'):
        return ans[start][finish]
    else:
        return -1


if __name__ == '__main__':
    print(main())
