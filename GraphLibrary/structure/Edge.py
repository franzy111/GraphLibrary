class Edge:
    def __init__(self, start, finish, weight=0):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __iter__(self):
        return iter((self.start, self.finish))

    def get_weight(self):
        return self.weight
