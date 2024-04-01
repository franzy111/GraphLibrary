import unittest
from GraphLibrary.structure import *
from GraphLibrary.algorithms import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        graph = Graph()
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(2, 3, 1))
        graph.add_edge(Edge(2, 4, 3))
        graph.add_edge(Edge(3, 4, 1))
        path = dijkstra(4, 1, 4, graph)
        self.assertEqual([1, 3, 4], path)


if __name__ == '__main__':
    unittest.main()
