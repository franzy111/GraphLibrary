import unittest
from GraphLibrary.structure import Graph, Edge
from GraphLibrary.algorithms import ford_bellman


class TestFordBellman(unittest.TestCase):
    def test_ford_bellman(self):
        graph = Graph()
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(2, 3, 1))
        graph.add_edge(Edge(2, 4, 3))
        graph.add_edge(Edge(3, 4, 1))
        path = ford_bellman(4, graph, 1, 4)
        self.assertEqual([1, 3, 4], path)


if __name__ == '__main__':
    unittest.main()
