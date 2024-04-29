from GraphLibrary import Graph, Edge
from GraphLibrary.algorithms import ford_bellman
import random_graphs_generator
from help_for_stats import test
from random import randint


def worst_graph_for_ford(n: int) -> Graph:
    graph = Graph()
    for i in range(n):
        for j in range(i):
            graph.add_edge(Edge(j, i, randint(-100_000, 100_000)))
    return graph


def test_ford_best():
    with open('results/ford_test_best.txt', 'w') as f:
        for i in range(2, 100, 2):
            print(i)
            f.write(str(i) + " " + "%.6f" % test(20, ford_bellman, i,
                                                 random_graphs_generator.get_tree(i, True),
                                                 0, 1) + "\n")


def test_ford_worst():
    with open('results/ford_test_worst.txt', 'w') as f:
        for i in range(1, 100, 2):
            print(i)
            f.write(str(i) + " " + "%.6f" % test(20, ford_bellman, i,
                                                 worst_graph_for_ford(i), 0, 1) + "\n")


def test_ford_random():
    with open('results/ford_test_random.txt', 'w') as f:
        for i in range(1, 100, 2):
            print(i)
            f.write(str(i) + " " + "%.6f" % test(20, ford_bellman, i,
                                                 random_graphs_generator.get_connected_graph(i),
                                                 0, i - 1) + "\n")


if __name__ == '__main__':
    test_ford_best()
    test_ford_worst()
    test_ford_random()
