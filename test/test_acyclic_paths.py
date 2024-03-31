import unittest
from GraphLibrary.structure.Graph import Graph
from GraphLibrary.structure.Edge import Edge
from GraphLibrary.algorithms import acyclic_paths


class TestAcyclicPaths(unittest.TestCase):
    def test_acyclic_paths(self):
        # Создаем граф
        graph = Graph()
        # Добавляем вершины и ребра в граф
        graph.add_edge(Edge(0, 1, 5))
        graph.add_edge(Edge(0, 2, 3))
        graph.add_edge(Edge(1, 3, 6))
        graph.add_edge(Edge(1, 2, 2))
        graph.add_edge(Edge(2, 4, 4))
        graph.add_edge(Edge(2, 5, 2))
        graph.add_edge(Edge(2, 3, 7))
        graph.add_edge(Edge(3, 4, -1))
        graph.add_edge(Edge(4, 5, -2))

        # Вызываем функцию, которую мы тестируем
        path = acyclic_paths(graph, 6, 0, 5)

        # Проверяем, что найденный путь верен
        self.assertEqual(path, [1, 3, 4, 6])


if __name__ == '__main__':
    unittest.main()
