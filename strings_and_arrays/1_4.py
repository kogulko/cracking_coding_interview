import doctest
import collections
def polyndrom_replace(string):
    """
    >>> polyndrom_replace('Tact Coa')
    True
    """
    letters = collections.defaultdict(int)
    for i in string:
        letters[i] += 1
    return len([i for i in letters.values() if i % 2 != 0]) == 1




if __name__ == '__main__':
    doctest.testmod()
