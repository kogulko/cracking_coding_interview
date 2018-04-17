def permutation_check(a, b):
    'Check if one string is permutation of another'
    print('Is permutation' if quicksort(list(a)) == quicksort(list(b)) else 'Not permutation')


def quicksort(a):
    if len(a) < 2:
        return a
    pivot = a.pop(0)
    return quicksort(list(filter(lambda c: c < pivot, a))) + \
           [pivot] + \
           quicksort(list(filter(lambda c: c > pivot, a)))


permutation_check('smth', 'tmsh')
permutation_check('smth', 'tmsw')
permutation_check('hsmt', 'tshm')
