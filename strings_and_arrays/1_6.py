import doctest
import collections

def simple_encoding(string):
    """
    >>> simple_encoding('aabcccccaaa')
    'a2b1c5a3'
    >>> simple_encoding('abcdef')
    'abcdef'
    """
    res = ''
    i = 0
    count = 0
    char = string[0]
    while i < len(string):
        if char == string[i]:
            count += 1
        else:
            res += char + str(count)
            char = string[i]
            count = 1
        i += 1
    else:
        res += char + str(count)
    return res if len(string) > len(res) else string




if __name__ == '__main__':
    doctest.testmod()
