

class Graph(object):

    def __init__(self):
        self.graph = {}

    def add_node(self, s, v):
        if s in self.graph:
            self.graph[s].append(v)
            return
        self.graph[s] = [v]

    def remove_node(self, s, v):
        if s not in self.graph:
            raise ValueError("Specified source doesn't exist in the adjacency list")
        index = self.graph[s].index(v)
        del self.graph[s][index]

    def print_graph(self):
        for s in self.graph:
            print(f"{s} -> {self.graph[s]}")


def main():
    graph = Graph()
    graph.add_node('a', 's')
    graph.add_node('a', 'z')
    graph.add_node('z', 'a')
    graph.add_node('s', 'a')
    graph.add_node('s', 'x')
    graph.add_node('x', 's')
    graph.add_node('x', 'd')
    graph.add_node('x', 'c')
    graph.add_node('c', 'x')
    graph.add_node('c', 'd')
    graph.add_node('d', 'x')
    graph.add_node('d', 'c')

    graph.print_graph()


if __name__ == '__main__':
    main()
