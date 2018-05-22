from one_way_linked_list import *
import doctest

def polyndrome(a):
        """
        >>> polyndrome([7,1,6])
        False
        >>> polyndrome([1,2,3,4,5,4,3,2,1])
        True
        >>> polyndrome([2,2,6,6,2,2,2,2,6,6,2,2])
        True
        """
        N = len(a)
        l = LinkedList()
        stack = []
        for i in reversed(a):
            l.add(i)
        node = l.head
        while len(stack) < N // 2:
            stack.append(node.data)
            node = node.next
        if N % 2 == 1:
            node = node.next
        while node:
            if stack.pop() != node.data:
                return False
            node = node.next
        return True
if __name__ == '__main__':
        doctest.testmod()
