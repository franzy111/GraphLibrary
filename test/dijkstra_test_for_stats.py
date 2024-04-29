from GraphLibrary import Graph, Edge
from GraphLibrary.algorithms import dijkstra
import random_graphs_generator
from help_for_stats import test

def best_graph_for_dijkstra(n: int) -> Graph:
    graph = Graph()
    for i in range(n):
        for j in range(i):
            if j == 0 and i == 1:
                graph.add_edge(Edge(j, i, 1))
            else:
                graph.add_edge(Edge(j, i, 2))
    return graph


def worst_graph_for_dijkstra(n: int) -> Graph:
    # TODO
    pass


def test_dijkstra_best():
    with open('results/dijkstra_test_best.txt', 'w') as f:
        for i in range(2, 1000, 2):
            f.write(str(i) + " " + "%.6f" % test(20, dijkstra, i, 0, 1, best_graph_for_dijkstra(i)) + "\n")


def test_dijkstra_worst():
    with open('results/dijkstra_test_worst.txt', 'w') as f:
        for i in range(1, 300, 2):
            f.write(str(i) + " " + "%.6f" % test(20, dijkstra, i, 0, 1, worst_graph_for_dijkstra(i)) + "\n")


def test_dijkstra_random():
    with open('results/dijkstra_test_random.txt', 'w') as f:
        for i in range(1, 500, 2):
            f.write(str(i) + " " + "%.6f" % test(20, dijkstra, i, 0, i - 1,
                                                 random_graphs_generator.get_connected_graph(i)) + "\n")


if __name__ == "__main__":
    test_dijkstra_best()
    # test_dijkstra_worst()
    test_dijkstra_random()
