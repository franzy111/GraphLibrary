from GraphLibrary.structure.Graph import Graph

'''
Самая простейшая реализация
Будем ли оптимизировать? Есть улучшенный алгоритм SPFA, но как будто это вообще отдельный алгоритм
Ещё код не учитывает, что в графе могут быть отрицательные циклы, надо ли добавлять?
Как вообще подаётся граф? Преобразование вынесем в отдельный файл?
По-хорошему надо бы для ребра создать отдельный класс, у которого будет три поля: начало, конец, вес
'''


def ford_bellman(n: int, graph: Graph, start: int, finish: int) -> list:
    # n + 1, потому что решил, что пока что будем работать в 1-индексации
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
    return get_path(finish, parent)


def get_path(finish: int, parent: list) -> list:
    v = finish
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]
