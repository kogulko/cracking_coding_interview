class Node:
    def __init__(self, data):
        self.visited = False
        self.adjacent = []
        self.data = data

    def push(self, node):
        self.adjacent.append(node)

    def __str__(self):
        return self.data


class Graph:
    def __init__(self, nodes):
        self.nodes = []
        for parent, children in nodes.items():
            for child in children:
                self.push_to_node(parent, child)

    def find__or_initialize_node(self, data):
        return next(
            (node for node in self.nodes if node.data == data),
            Node(data))

    def push_to_node(self, root, to):
        parent = self.find__or_initialize_node(root)
        self.push(parent)
        child = self.find__or_initialize_node(to)
        self.push(child)
        parent.push(child)

    def push(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def visit(self, node):
        node.visited = True

    def dfs_search(self, root, to):
        if not root:
            return False
        self.visit(root)
        for node in root.adjacent:
            if node.data == to:
                return True
            elif not node.visited:
                return self.dfs_search(node, to)
