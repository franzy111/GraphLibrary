import unittest
from GraphLibrary.structure import *
from GraphLibrary.algorithms import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        # Создаем граф
        graph = Graph()
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(2, 3, 1))
        graph.add_edge(Edge(2, 4, 3))
        graph.add_edge(Edge(3, 4, 1))

        # Вызываем функцию, которую мы тестируем
        path = dijkstra(4, 1, 4, graph)

        # Проверяем, что найденный путь верен
        self.assertEqual(path, [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
