from one_way_linked_list import *
import doctest

def breaking(l, k):
        """
        >>> breaking([2,3,5,1,6,2,4,7,10], 5)
        4 --> 2 --> 1 --> 3 --> 2 --> 10 --> 7 --> 6 --> 5
        >>> breaking([2,3,5,1,6,2,4,7,10], 2)
        1 --> 10 --> 7 --> 4 --> 2 --> 6 --> 5 --> 3 --> 2
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
                less.add(node.data)
                tail = node
            else:
                more.add(node.data)

            node = node.next
        node = less.head
        while node.next:
            node = node.next
        else:
            node.next = more.head
        print(less)

if __name__ == '__main__':
        doctest.testmod()
