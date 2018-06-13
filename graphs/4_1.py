from graph import Graph


def find_path(nodes, start, end):
    graph = Graph(nodes)
    root = graph.find__or_initialize_node(start)
    return graph.dfs_search(root, end)


nodes = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'E'],
         'E': ['F'],
         'F': ['C']}

res = find_path(nodes, 'B', 'A')
print(res)
