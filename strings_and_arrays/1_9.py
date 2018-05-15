import doctest

def shift_check(s1, s2):
        """
        >>> shift_check('waterbottle', 'erbottlewat')
        True
        >>> shift_check('waterbottle', 'rebottlewat')
        False
        >>> shift_check('abcdefg', 'defgabc')
        True
        """
        return is_substring(s2 * 2, s1)

def is_substring(s1, s2):
    return s2 in s1

if __name__ == '__main__':
        doctest.testmod()
