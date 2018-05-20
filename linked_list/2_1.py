from linked_list import *
import collections
import doctest

def remove_dublicates(l):
        """
        >>> remove_dublicates([1,1,1,2,2,5,3,4,6,6,2,7,8,8,9,9,9,10])
        1 --> 2 --> 5 --> 3 --> 4 --> 6 --> 7 --> 8 --> 9 --> 10
        """
        linked = LinkedList()
        for i in reversed(l):
            linked.add(i)
        counter = collections.defaultdict(int)
        node = linked.head
        while node is not None:
            if counter[node.data] == 0:
                counter[node.data] += 1
            else:
                linked.remove(node)
            node = node.next
        print(linked)


if __name__ == '__main__':
        doctest.testmod()

linked = LinkedList()

