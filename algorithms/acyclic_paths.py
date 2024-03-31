from structure.Graph import Graph

# Будем ли предварительно проверять граф на ацикличность?
# Ориентированный ациклический граф
MAXN = 100_000
order = []  # Мне кажется так делать нехорошо, но ничего лучше уже придумать не могу
used = [False] * MAXN  # Тоже плохо
parent = [-1] * MAXN


# Может dfs как-то отдельно вынести?
def dfs(v: int, graph: Graph, n: int) -> None:
    used[v] = True
    for to, weight in graph.get_adjacent_nodes(v):
        if not used[to]:
            dfs(to, graph, n)
    order.append(v)


def topological_sort(graph: Graph, n: int) -> list:
    for v in range(n):
        if not used[v]:
            dfs(v, graph, n)
    order.reverse()
    return order


def acyclic_paths(graph: Graph, n: int, start: int) -> list:
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    topologicalsort = topological_sort(graph, n)
    for v in topologicalsort:
        for to, weight in graph.get_adjacent_nodes(v):
            if distance[v] != float('inf') and distance[to] > distance[v] + weight:
                distance[to] = distance[v] + weight
                parent[to] = v
    return distance


# Совпадает ещё у двух алгоритмов, можно вынести в отдельный метод как-будто
def get_path(finish: int) -> list:
    v = finish
    path = []
    while v != -1:
        # Потому что мы в 0-индексации, а хотим печать в 1-индексации
        path.append(v + 1)
        v = parent[v]
    return path[::-1]


'''
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
        return ans[finish], get_path(finish)
    else:
        return -1


if __name__ == '__main__':
    print(main())
'''
