

class Graph:
    def __init__(self, graph=None):
        self._graph = graph if graph else {}

    def get_edges(self, v):
        return self._graph[v]

    def vertices(self):
        return self._graph.keys()

    def all_edges(self):
        return self._graph.values()

    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] = []

    def add_edge(self, e, v):
        if v in self._graph and e in self._graph:
            self._graph[v].append(e)
            self._graph[e].append(v)
        else:
            self.add_vertex(v)
            self.add_vertex(e)
            self.add_edge(e, v)

    def __repr__(self):
        graph_repr = ''
        for v, e in self._graph.items():
            graph_repr = graph_repr + f"{v} --> {e}\n"
        return graph_repr


graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,7)
graph.add_edge(1,8)
graph.add_edge(2,6)
graph.add_edge(3,2)
graph.add_edge(3,8)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(7,6)

print(graph)




