from .Graph import Graph
from .Edge import Edge


class DirGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge: Edge) -> None:
        first_node, second_node = edge
        if first_node not in self.adjacency_list:
            self.adjacency_list[first_node] = []
        if second_node not in self.adjacency_list:
            self.adjacency_list[second_node] = []

        if second_node in self.adjacency_list[first_node]:
            raise ValueError("There is already such a nodes in the graph")

        self.adjacency_list[first_node].append(second_node)
        self.list_of_edges[(first_node, second_node)] = edge
