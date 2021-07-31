from data_structures.graph import Graph
from data_structures.stack import Stack
from data_structures.queue import Queue

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


def dfs(graph):
    visited = Stack()
    dfs_traverse(1, visited, graph)
    return visited

def dfs_traverse(v, visited, graph):
    visited.add(v)
    for next_edge in graph.get_edges(v):
        print(f" {v} next edge: {next_edge} in {graph.get_edges(v)} {next_edge in visited}")
        if next_edge not in visited:
            dfs_traverse(next_edge, visited, graph)



def bfs_traverse(v, graph):
    visited, queue = set(), Queue()
    queue.add(v)
    visited.add(v)
    result = []
    while not queue.is_empty():
        # Dequeue a vertex from queue
        vertex = queue.pop()
        result.append(vertex)
        # If not visited, mark it as visited, and enqueue it
        for edge in graph.get_edges(vertex):
            if edge not in visited:
                visited.add(edge)
                queue.add(edge)

    return result


def bfs(graph):
    res = bfs_traverse(1,  graph)
    return res

print(bfs(graph))
print('--------------------------------------------')
# print(dfs(graph))