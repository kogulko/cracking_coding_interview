from one_way_linked_list import *
import doctest

def find_k(l, k):
        """
        >>> find_k([1,2,3,4,5,6,7,8,9,10], 2)
        9
        >>> find_k([1,2,3,4,5,6,7,8,9,10], 4)
        7
        >>> find_k([1,2,3,4,5,6,7,8,9,10], 8)
        3
        """
        linked = LinkedList(l)
        fast = linked.head
        slow = linked.head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.data

if __name__ == '__main__':
        doctest.testmod()
