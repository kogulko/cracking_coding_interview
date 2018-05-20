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
        rows = []
        columns = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
                    break
        nullify_rows(rows, matrix)
        nullify_columns(columns, matrix)
        print(matrix)

def nullify_rows(rows, matrix):
    for i in rows:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

def nullify_columns(columns, matrix):
    for i in columns:
        for j in range(len(matrix[i])):
            matrix[j][i] = 0

if __name__ == '__main__':
        doctest.testmod()
