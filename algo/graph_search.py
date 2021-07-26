from data_structures.graph import Graph
from data_structures.stack import Stack
from data_structures.queue import Queue



graph = Graph(graph={1:[2,3,4]})

def bfs(graph):
    visited = [False] * len(graph)


def dfs_traverse(v, visited, graph):
    visited.add(v)
    for next_v in graph[v]:
        if next_v not in visited:
            dfs_traverse(next_v, visited, graph)


def dfs(graph, v):
    visited = Stack()
    dfs_traverse(v, visited, graph)

