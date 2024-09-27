#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n // 2)):
         y = n - i - 1
        for j in range(i, y):
            x = n - 1 - j
            # Perform a 4-way swap to rotate the matrix
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]    # Top -> Left
            matrix[x][i] = matrix[y][x]    # Left -> Bottom
            matrix[y][x] = matrix[j][y]    # Bottom -> Right
            matrix[j][y] = tmp             # Right -> Top
