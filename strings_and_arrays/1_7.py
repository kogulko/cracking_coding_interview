import doctest
import numpy as np
N = 101


def transponse():
    """
    >>> transponse()
    True
    >>> transponse()
    True
    """
    matrix = np.random.randint(0, 99, (N, N))
    rotated = np.zeros(shape=(N, N))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rotated[N - 1 - j][i] = matrix[i][j]
    return np.array_equal(rotated, np.rot90(matrix))

if __name__ == '__main__':
    doctest.testmod()
