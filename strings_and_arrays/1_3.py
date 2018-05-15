import doctest
def replace_spaces(string):
    """
    >>> replace_spaces('Mr John Smith')
    'Mr%20John%20Smith'
    """
    return ''.join(['%20' if i == ' ' else i for i in string])

if __name__ == '__main__':
    doctest.testmod()
