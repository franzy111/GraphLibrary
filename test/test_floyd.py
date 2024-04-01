import unittest
from GraphLibrary.structure import Graph, Edge
from GraphLibrary.algorithms import floyd_warshall


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        graph = Graph()
        graph.add_edge(Edge(0, 1, 1))
        graph.add_edge(Edge(0, 2, 2))
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 3))
        graph.add_edge(Edge(2, 3, 1))
        path = floyd_warshall(4, graph, 0, 3)
        self.assertEqual([0, 2, 3], path)


if __name__ == '__main__':
    unittest.main()
