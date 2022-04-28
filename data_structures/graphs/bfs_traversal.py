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

    def bfs_print(self, s):
        visited = [s]
        unvisited = [s]

        while unvisited:

            # Pop from unseen
            vertex = unvisited.pop(0)

            for v in self.graph[vertex]:
                if v not in visited:
                    visited.append(v)
                    unvisited.append(v)

        print("BFS: ")
        print(visited)

    def print_graph(self):
        for s in self.graph:
            print(f"{s} -> {self.graph[s]}")


def main():
    graph = Graph()
    graph.add_node(0, 1)
    graph.add_node(0, 2)
    graph.add_node(0, 3)
    graph.add_node(1, 0)
    graph.add_node(1, 2)
    graph.add_node(1, 4)
    graph.add_node(3, 0)
    graph.add_node(2, 0)
    graph.add_node(2, 1)
    graph.add_node(2, 4)
    graph.add_node(4, 2)

    graph.print_graph()
    graph.bfs_print(s=0)


if __name__ == '__main__':
    main()
