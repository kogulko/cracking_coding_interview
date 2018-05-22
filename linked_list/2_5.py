from one_way_linked_list import *
import doctest

def addition(a, b):
        """
        >>> addition([7,1,6], [5,9,2])
        9 --> 1 --> 2
        >>> addition([8,6,5], [0,0,0,1])
        1 --> 5 --> 6 --> 8
        """
        l_a = LinkedList()
        l_b = LinkedList()
        for i in reversed(a):
            l_a.add(i)
        for i in reversed(b):
            l_b.add(i)
        res = LinkedList()
        node_a = l_a.head
        node_b = l_b.head
        floor = 0
        module = 0
        while (node_a is not None) or (node_b is not None):
            if node_a:
                a = node_a.data
                node_a = node_a.next
            else:
                a = 0
            if node_b:
                b = node_b.data
                node_b = node_b.next
            else:
                b = 0
            add = a + b + floor
            floor = add // 10
            module = add % 10
            res.add(module)
        print(res)
if __name__ == '__main__':
        doctest.testmod()
