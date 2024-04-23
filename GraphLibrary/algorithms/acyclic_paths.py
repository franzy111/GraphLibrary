from GraphLibrary.structure.Graph import Graph


# Будем ли предварительно проверять граф на ацикличность?
# Ориентированный ациклический граф


# Может dfs как-то отдельно вынести?
def dfs(v: int, graph: Graph, n: int, order: list, used: list) -> None:
    """
    Выполняет обход в глубину графа, начиная с вершины v.

    :param v: (int): Индекс текущей вершины.
    :param graph: (Graph): Граф, в котором нужно выполнить обход в глубину.
    :param n: (int): Количество вершин в графе.
    :param order: (list): Список для сохранения порядка обхода.
    :param used: (list): Список, отмечающий использованные вершины.

    :return: None
    """
    used[v] = True
    list_of_adj = graph.get_adjacent_nodes(v)
    for to in list_of_adj:
        if not used[to]:
            dfs(to, graph, n, order, used)
    order.append(v)


def topological_sort(graph: Graph, n: int) -> list:
    """
    Выполняет топологическую сортировку графа.

    :param graph: (Graph): Граф, для которого нужно выполнить топологическую сортировку.
    :param n: (int): Количество вершин в графе.

    :return: Список, содержащий вершины в порядке топологической сортировки.
    """
    order = []
    used = [False] * n
    for v in range(n):
        if not used[v]:
            dfs(v, graph, n, order, used)
    order.reverse()
    return order


def acyclic_paths(graph: Graph, n: int, start: int, finish: int) -> list:
    """
       Находит кратчайший путь в ацикличном графе от начальной до конечной вершины.

       :param graph: (Graph): Граф, в котором нужно найти кратчайший путь.
       :param n: (int): Количество вершин в графе.
       :param start: (int): Индекс начальной вершины.
       :param finish: (int): Индекс конечной вершины.

       :return: Список, представляющий кратчайший путь от начальной до конечной вершины.

       Примечания: этот метод работает только для ацикличных графов.
       """
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    parent = [-1] * n
    topologicalsort = topological_sort(graph, n)
    for v in topologicalsort:
        list_of_adj = graph.get_adjacent_nodes(v)
        for to in list_of_adj:
            weight = graph.get_weight_edge(v, to)
            if distance[v] != float('inf') and distance[to] > distance[v] + weight:
                distance[to] = distance[v] + weight
                parent[to] = v
    return _get_path(finish, parent)


# Совпадает ещё у двух алгоритмов, можно вынести в отдельный метод как-будто
def _get_path(finish: int, parent: list) -> list:
    v = finish
    path = []
    while v != -1:
        # Потому что мы в 0-индексации, а хотим печать в 1-индексации
        path.append(v)
        v = parent[v]
    return path[::-1]
