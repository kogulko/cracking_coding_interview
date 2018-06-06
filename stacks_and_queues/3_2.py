import doctest

def min_stack(l):
        """
        >>> min_stack([3,4,5,6,7,2,1,3,5,6,7])
        1
        >>> min_stack([9,8,7,6,5,7,8,9,1,5,7,5,3,5,7])
        1
        >>> min_stack([7,5,6,5,4,6,6,4,3,5,2,7, -282, 6,4,45])
        -282
        """
        first = l.pop(0)
        stack = [{ 'min': first, 'val': first }]
        for i in l:
            stack.insert(0, { 'min': min(i, stack[0]['min']), 'val': i })
        return stack[0]['min']
if __name__ == '__main__':
        doctest.testmod()
