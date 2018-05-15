import doctest
def uniq_symbols(string):
    """
    >>> uniq_symbols('something')
    Uniq!
    >>> uniq_symbols('My name is Alex')
    Symbols is not uniq
    >>> uniq_symbols('abcdefg')
    Uniq!
    """
    string = sorted(string)
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            print('Symbols is not uniq')
            break
    else:
        print('Uniq!')

if __name__ == '__main__':
    doctest.testmod()
