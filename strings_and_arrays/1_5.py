import doctest
import collections

def modifications_count(a, b):
    """
    >>> modifications_count('pale', 'ple')
    True
    >>> modifications_count('pales', 'pale')
    True
    >>> modifications_count('pale', 'bale')
    True
    >>> modifications_count('pale', 'bake')
    False
    >>> modifications_count('Tuunbak', 'Tunbak')
    True
    """
    letters = collections.defaultdict(int)
    n = len(a) if len(a) > len(b) else len(b)
    for i in range(n):
        if i < len(a):
            letters[a[i]] += 1
        if i < len(b):
            letters[b[i]] -= 1
    return len([i for i in letters.values() if i != 0]) < 3





if __name__ == '__main__':
    doctest.testmod()
