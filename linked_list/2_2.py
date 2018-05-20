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
        linked = LinkedList()
        for i in reversed(l):
            linked.add(i)
        pointers = [linked.head]
        while True:
            for i in range(len(pointers)):
                if pointers[i].next is None:
                    return pointers[-1].data
                else:
                    pointers[i] = pointers[i].next

            if len(pointers) < k:
                pointers.append(linked.head)

if __name__ == '__main__':
        doctest.testmod()
