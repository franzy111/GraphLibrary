from structure.Graph import Graph

'''
Самая простейшая реализация
Будем ли оптимизировать? Есть улучшенный алгоритм SPFA, но как будто это вообще отдельный алгоритм
Ещё код не учитывает, что в графе могут быть отрицательные циклы, надо ли добавлять?
Как вообще подаётся граф? Преобразование вынесем в отдельный файл?
По-хорошему надо бы для ребра создать отдельный класс, у которого будет три поля: начало, конец, вес
'''

parent = [-1] * 100_000  # ПЛОХО!!! что глобальная, потом что-то придумаем :))


def ford_bellman(n: int, graph: Graph, start: int) -> list:
    # n + 1, потому что решил, что пока что будем работать в 1-индексации
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    edges = graph.get_edges()
    for i in range(n - 1):
        for edge in edges:
            a, b, w = edge
            if distance[b] > distance[a] + w:
                distance[b] = distance[a] + w
                parent[b] = a
    return distance


def get_path(finish: int) -> list:
    v = finish
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]

# Старый main, изначально делал, чтобы тестить алгоритм, теперь думаю не нужен
'''
def main():
    # Очевидно переделать считывание
    n, m, start, finish = map(int, input().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    ans = ford_bellman(n, edges, start)
    if ans[finish] != float('inf'):
        return ans[finish], get_path(finish)
    else:
        return -1


if __name__ == '__main__':
    print(main())
'''
