# Будем ли предварительно проверять граф на ацикличность?
# Ориентированный ациклический граф
MAXN = 100_000
order = []  # Мне кажется так делать нехорошо, но ничего лучше уже придумать не могу
used = [False] * MAXN  # Тоже плохо


def dfs(v: int, graph: list, n: int) -> None:
    used[v] = True

    for to, weight in graph[v]:
        if not used[to]:
            dfs(to, graph, n)
    order.append(v)


def topological_sort(graph: list, n: int) -> list:
    for v in range(n):
        if not used[v]:
            dfs(v, graph, n)
    order.reverse()
    return order


def acyclic_paths(graph: list, n: int, start: int) -> list:
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    topologicalsort = topological_sort(graph, n)
    for v in topologicalsort:
        for to, weight in graph[v]:
            if distance[v] != float('inf') and distance[to] > distance[v] + weight:
                distance[to] = distance[v] + weight
    return distance


def main():
    n, m, start, finish = map(int, input().split())
    start -= 1
    finish -= 1
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, w = map(int, input().split())
        # 0-индексация
        a -= 1
        b -= 1
        graph[a].append((b, w))
    ans = acyclic_paths(graph, n, start)
    if ans[finish] != float('inf'):
        return ans[finish]
    else:
        return -1


if __name__ == '__main__':
    print(main())
