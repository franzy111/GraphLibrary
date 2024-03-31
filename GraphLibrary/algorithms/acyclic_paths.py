from GraphLibrary.structure.Graph import Graph

# Будем ли предварительно проверять граф на ацикличность?
# Ориентированный ациклический граф


# Может dfs как-то отдельно вынести?
def dfs(v: int, graph: Graph, n: int, order: list, used: list) -> None:
    used[v] = True
    for to, weight in graph.get_adjacent_nodes(v):
        if not used[to]:
            dfs(to, graph, n)
    order.append(v)


def topological_sort(graph: Graph, n: int) -> list:
    order = []
    used = [False] * n
    for v in range(n):
        if not used[v]:
            dfs(v, graph, n, order, used)
    order.reverse()
    return order


def acyclic_paths(graph: Graph, n: int, start: int, finish: int) -> list:
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    parent = [-1] * n
    topologicalsort = topological_sort(graph, n)
    for v in topologicalsort:
        for to, weight in graph.get_adjacent_nodes(v):
            if distance[v] != float('inf') and distance[to] > distance[v] + weight:
                distance[to] = distance[v] + weight
                parent[to] = v
    return get_path(finish, parent)


# Совпадает ещё у двух алгоритмов, можно вынести в отдельный метод как-будто
def get_path(finish: int, parent: list) -> list:
    v = finish
    path = []
    while v != -1:
        # Потому что мы в 0-индексации, а хотим печать в 1-индексации
        path.append(v + 1)
        v = parent[v]
    return path[::-1]
