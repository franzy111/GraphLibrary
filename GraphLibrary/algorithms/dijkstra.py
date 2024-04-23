from queue import PriorityQueue
from GraphLibrary.structure.Graph import Graph

"""
Над чем подумать:
1) В дейкстре нельзя, чтобы были отрицательные веса, нужна ли эта предварительная проверка?
2) Если очень сильно хочется, то можно реализовать свою структуру данных с приоритетами, которая
    за логарифм будет брать минимум. Но приоритетная очередь по-моему хороша, но если самим делать 
    то надо Фибоначчиеву кучу делать 
"""


def dijkstra(n: int, start: int, finish: int, graph: Graph) -> list:
    """
    Выполняет алгоритм Дейкстры для поиска кратчайшего пути в графе.

    :param n: (int): Количество вершин в графе.
    :param start: (int): Индекс начальной вершины.
    :param finish: (int): Индекс конечной вершины.
    :param graph: (Graph): Граф, в котором нужно найти кратчайший путь.

    :return: Список вершин, представляющий кратчайший путь от начальной до конечной вершины.

    Примечания: не поддерживает отрицательные веса.
    """
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    parent = [-1] * (n + 1)
    processed = [False for _ in range(n + 1)]
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        curr_dist, v = pq.get()
        if processed[v]:
            continue
        processed[v] = True
        list_of_adj = graph.get_adjacent_nodes(v)
        for to in list_of_adj:
            w = graph.get_weight_edge(v, to)
            if distance[to] > distance[v] + w:
                distance[to] = distance[v] + w
                parent[to] = v
                pq.put((distance[to], to))
    return _get_path(start, finish, parent)


def _get_path(start: int, finish: int, parent: list) -> list:
    v = finish
    path = []
    while v != start:
        path.append(v)
        v = parent[v]
    path.append(start)
    return path[::-1]
