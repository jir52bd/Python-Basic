
class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_edage(self, x, y):
        if x not in self.adj_list:
            self.adj_list[x] = []
        if y not in self.adj_list:
            self.adj_list[y] = []

        self.adj_list[x].append(y)
        self.adj_list[y].append(x)

    def display(self):
        for vartex, neighbours in self.adj_list.items():
            print(f"{vartex} --> ", end=' ')
            for neighbour in neighbours:
                print(neighbour, end=' ')
            print('')


g = Graph()

g.add_edage(1, 2)
g.add_edage(1, 3)
g.add_edage(3, 4)
g.add_edage(3, 5)

g.display()