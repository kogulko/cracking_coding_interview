class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, list):
        self.head = None
        for i in reversed(list):
            self.add(i)

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def push(self, node):
        p = self.head
        if p is not None:
            while p.next:
                p = p.next
            p.next = node
        else:
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
        if not (p and p.next):
            return False
        p.data = p.next.data
        p.next = p.next.next
        return True


    def __str__(self):
        _head = self.head
        value = ''
        while _head:
            value += str(_head.data)+" --> "
            _head = _head.next
        return value[0:-5]
