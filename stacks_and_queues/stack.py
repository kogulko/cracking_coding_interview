class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0
