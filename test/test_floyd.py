import unittest
from GraphLibrary.structure import Graph, Edge
from GraphLibrary.algorithms import floyd_warshall


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        # Создаем граф
        graph = Graph()
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(2, 3, 1))
        graph.add_edge(Edge(2, 4, 3))
        graph.add_edge(Edge(3, 4, 1))

        # Вызываем функцию, которую мы тестируем
        path = floyd_warshall(4, graph, 1, 4)

        # Проверяем, что найденный путь верен
        self.assertEqual(path, [1, 2, 4])


if __name__ == '__main__':
    unittest.main()
