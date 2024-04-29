from GraphLibrary import Graph, Edge
from GraphLibrary.algorithms import floyd_warshall
import random_graphs_generator
from help_for_stats import test


def any_floyd_warshall_test():
    with open('results/floyd_warshall_any.txt', 'w') as f:
        for i in range(1, 500, 2):
            print(i)
            f.write(str(i) + " " + "%.6f" % test(20, floyd_warshall, i,
                                                 random_graphs_generator.get_connected_graph(i),
                                                 0, i - 1) + "\n")


if __name__ == '__main__':
    any_floyd_warshall_test()
