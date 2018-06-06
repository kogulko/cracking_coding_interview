class StackOfStacks:
    N = 5

    def __init__(self, data):
        self.stacks = [[]]

    def push(self, value):
        if len(self.stacks[0]) < StackOfStacks.N:
            self.stacks[0].insert(0, value)
        else:
            self.stacks.insert(0, [value])

    def pop_at(self, i):
        if len(self.stacks[i]) > 1:
            return self.stacks[i].pop(0)
        else:
            return self.stacks.pop(i)[0]
