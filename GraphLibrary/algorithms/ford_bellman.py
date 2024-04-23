from GraphLibrary.structure.Graph import Graph

'''
Самая простейшая реализация
Будем ли оптимизировать? Есть улучшенный алгоритм SPFA, но как будто это вообще отдельный алгоритм
Ещё код не учитывает, что в графе могут быть отрицательные циклы, надо ли добавлять?
Как вообще подаётся граф? Преобразование вынесем в отдельный файл?
По-хорошему надо бы для ребра создать отдельный класс, у которого будет три поля: начало, конец, вес
'''


def ford_bellman(n: int, graph: Graph, start: int, finish: int) -> list:
    """
    Находит кратчайший путь от начальной вершины до конечной вершины в графе,
    используя алгоритм Беллмана-Форда.

    :param n: (int): Количество вершин в графе.
    :param graph: (Graph): Граф, в котором нужно найти кратчайший путь.
    :param start: (int): Индекс начальной вершины.
    :param finish: (int): Индекс конечной вершины.

    :return: Список, представляющий кратчайший путь от начальной до конечной вершины.

    Примечания: не поддерживает отрицательные циклы.
    """
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    parent = [-1 for _ in range(n + 1)]
    edges = graph.get_edges()
    for i in range(n - 1):
        for edge in edges:
            a, b = edge
            w = edge.get_weight()
            if distance[b] > distance[a] + w:
                distance[b] = distance[a] + w
                parent[b] = a
    return _get_path(finish, parent)


def _get_path(finish: int, parent: list) -> list:
    v = finish
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]
