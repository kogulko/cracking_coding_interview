class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def remove(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev

    def __str__(self):
        _head = self.head
        value = ''
        while _head:
            value += str(_head.data)+" --> "
            _head = _head.next
        return value[0:-5]
