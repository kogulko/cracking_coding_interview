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
        l = LinkedList(a)
        stack = []
        fast = l.head
        slow = l.head
        while fast:
            if not fast.next:
                slow = slow.next
                break
            else:
                fast = fast.next.next
            stack.append(slow.data)
            slow = slow.next

        while slow:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
        return True
if __name__ == '__main__':
        doctest.testmod()
