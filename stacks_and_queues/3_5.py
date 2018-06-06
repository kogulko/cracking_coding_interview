from stack import *

import doctest

def sort(l):
    """
    >>> sort([4,5,6,2,6,7,3,6,7,3,2,1])
    [1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 7]
    """
    stack = Stack()
    temp_stack = Stack()
    for i in l:
        stack.push(i)

    while not stack.is_empty():
        tmp = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > tmp:
            stack.push(temp_stack.pop())

        temp_stack.push(tmp)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack.data

if __name__ == '__main__':
        doctest.testmod()
