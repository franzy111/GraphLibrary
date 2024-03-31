from queue import PriorityQueue
from structure.Graph import Graph

"""
Над чем подумать:
1) В дейкстре нельзя, чтобы были отрицательные веса, нужна ли эта предварительная проверка?
2) Если очень сильно хочется, то можно реализовать свою структуру данных с приоритетами, которая
    за логарифм будет брать минимум. Но приоритетная очередь по-моему хороша, но если самим делать 
    то надо Фибоначчиеву кучу делать 
"""
parent = [-1] * 100_000  # Думаю, что это плохо


def dijkstra(n: int, start: int, graph: Graph) -> list:
    # n + 1, потому что решил, что пока что будем работать в 1-индексации
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    processed = [False for _ in range(n + 1)]
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        curr_dist, v = pq.get()
        if processed[v]:
            continue
        processed[v] = True
        for to, w in graph.get_adjacent_nodes(v):
            if distance[to] > distance[v] + w:
                distance[to] = distance[v] + w
                parent[to] = v
                pq.put((distance[to], to))
    return distance


def get_path(start: int, finish: int) -> list:
    v = finish
    path = []
    while v != start:
        path.append(v)
        v = parent[v]
    path.append(start)
    return path[::-1]


'''
def main():
    n, m, start, finish = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    # Работает в 1-индексации
    # Считаем, что граф задаётся списком смежности и граф неориентированный
    # Проблемы: у нас n - должно быть количеством вершин, но не обязательно, что граф будет связный
    #           То есть может быть меньше чем n строк
    #           Можно сказать, что при считывании строка заканчивается всегда незначущим нулём
    #           Либо m раз передавать в формате: 4 2 3, что будет значить, что из 4 путь в 3 за цену 2
    #           UPD: пока что сделал последний вариант
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    ans = dijkstra(n, start, graph)
    if ans[finish] != float('inf'):
        return ans[finish], get_path(start, finish)
    else:
        return -1


if __name__ == '__main__':
    print(main())
'''
