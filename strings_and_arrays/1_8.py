import doctest

def nullify(matrix):
        """
        >>> nullify([[0,1,2],[3,0,5], [6,7,8]])
        [[0, 0, 0], [0, 0, 0], [0, 0, 8]]
        >>> nullify([[0,1,2],[3,6,5], [6,7,8]])
        [[0, 0, 0], [0, 6, 5], [0, 7, 8]]
        >>> nullify([[4,1,2],[3,0,5], [6,7,8]])
        [[4, 0, 2], [0, 0, 0], [6, 0, 8]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                elif matrix[i][j] == None:
                    for k in range(len(matrix[i])):
                        matrix[i][k] = 0
                        matrix[k][j] = 0
        print(matrix)


if __name__ == '__main__':
        doctest.testmod()
