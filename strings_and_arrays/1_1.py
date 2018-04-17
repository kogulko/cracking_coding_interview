def uniq_symbols(string):
    "Cheqk string for symbols uniquenes"
    for char in string:
        if string.count(char) > 1:
            print('Symbols is not uniq')
            break
    else:
        print('Uniq!')


uniq_symbols('something')
uniq_symbols('My name is Alex')
uniq_symbols('abcdefg')
