'''
Самая простейшая реализация
Будем ли оптимизировать? Есть улучшенный алгоритм SPFA, но как будто это вообще отдельный алгоритм
Ещё код не учитывает, что в графе могут быть отрицательные циклы, надо ли добавлять?
Как вообще подаётся граф? Преобразование вынесем в отдельный файл?
По-хорошему надо бы для ребра создать отдельный класс, у которого будет три поля: начало, конец, вес
'''


def ford_bellman(n: int, edges: list[tuple], start: int) -> list:
    # n + 1, потому что решил, что пока что будем работать в 1-индексации
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    for i in range(n - 1):
        for edge in edges:
            a, b, w = edge
            distance[b] = min(distance[b], distance[a] + w)
    return distance


def main():
    # Очевидно переделать считывание
    n, m, start, finish = map(int, input().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    ans = ford_bellman(n, edges, start)
    if ans[finish] != float('inf'):
        return ans[finish]
    else:
        return -1


if __name__ == '__main__':
    print(main())
