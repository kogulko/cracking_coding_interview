from one_way_linked_list import *
import doctest

def remove(l, k):
        """
        >>> remove([1,2,3,4,5,6,7,8,9,10], 8)
        1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 9 --> 10
        >>> remove([1,2,3,4,5,6,7,8,9,10], 4)
        1 --> 2 --> 3 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10
        >>> remove([1,2,3,4,5,6,7,8,9,10], 2)
        1 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10
        """
        linked = LinkedList()
        for i in reversed(l):
            linked.add(i)
        node = linked.head
        less = LinkedList()
        more = LinkedList()
        tail = None

        while node:
            if node.data < k:
                less.add(node)
                tail = node
            else:
                more.add(node)

            node = node.next
        print(linked)

if __name__ == '__main__':
        doctest.testmod()
