

class Graph:
    def __init__(self, graph=None):
        self._graph = graph if graph else {}

    def edges(self, v):
        return self._graph[v]

    def vertices(self):
        return self._graph.keys()

    def all_edges(self):
        return self._graph.values()

    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] = []




