from one_way_linked_list import *
import doctest
from collections import defaultdict

def intersection(a, b):
        """
        >>> intersection([7,1,6], [8,9,10,12,15])
        False
        >>> intersection([1,2,3,4,5,4,3,2,1], [1,5,6])
        True
        >>> intersection([1,2,3,4,5,6], [7,6,7])
        True
        """
        list_a = LinkedList(a)
        list_b = LinkedList(b)
        counts = defaultdict(int)
        node = list_a.head
        while node:
            counts[node.data] += 1
            node = node.next
        node = list_b.head
        while node:
            if counts[node.data] > 0:
                return True
            node = node.next
        else:
            return False
if __name__ == '__main__':
        doctest.testmod()
