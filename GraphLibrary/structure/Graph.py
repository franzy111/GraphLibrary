import Edge


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.list_of_edges = {}

    def get_nodes(self) -> list:
        return list(self.adjacency_list.keys())

    def get_edges(self) -> list:
        return list(self.list_of_edges.values())

    def get_adjacent_nodes(self, node) -> list:
        return self.adjacency_list[node]

    def add_node(self, node) -> None:
        if node in self.adjacency_list:
            raise ValueError("This node is already in the graph")
        self.adjacency_list[node] = []

    def add_edge(self, edge: Edge) -> None:
        first_node, second_node = edge
        if first_node not in self.adjacency_list or second_node not in self.adjacency_list:
            raise ValueError("Some of the nodes are not in the graph")
        if first_node in self.adjacency_list[second_node] or second_node in self.adjacency_list[first_node]:
            raise ValueError("There is already such a nodes in the graph")

        self.adjacency_list[first_node].append(second_node)
        self.adjacency_list[second_node].append(first_node)
        self.list_of_edges[(first_node, second_node)] = edge
        self.list_of_edges[(second_node, first_node)] = edge

    def delete_edge(self, edge: Edge) -> None:
        first_node, second_node = edge
        self.adjacency_list[first_node].remove(second_node)
        self.adjacency_list[first_node].remove(second_node)
        self.list_of_edges.pop((first_node, second_node))
        self.list_of_edges.pop((second_node, first_node))

    def get_incident_edge(self, first_node, second_node) -> Edge:
        return self.list_of_edges[(first_node, second_node)]

    def to_adjacency_matrix(self):
        vertices = self.get_nodes()
        adj_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        for edge in self.get_edges():
            first_node, second_node = edge
            first_node_index = vertices.index(first_node)
            second_node_index = vertices.index(second_node)
            # Как быть в случае ориентированого?
            adj_matrix[first_node_index][second_node_index] = edge.weight
            adj_matrix[second_node_index][first_node_index] = edge.weight
        return adj_matrix
