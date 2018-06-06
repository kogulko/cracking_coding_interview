from stack import Stack

class MyQueue:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def size(self):
        return len(self.stack_new) + len(self.stack_old)

    def add(self, value):
        self.stack_new.push(value)

    def remove(self):
        self.__shift_stacks()
        return self.stack_old.pop()

    def peek(self):
        self.__shift_stacks()
        return self.stack_old.peek()

    def __shift_stacks(self):
        if self.stack_old.is_empty():
            while not self.stack_new.is_empty():
                self.stack_old.push(self.stack_new.pop())
