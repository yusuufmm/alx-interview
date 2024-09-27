#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The input matrix to be rotated.
    """
    n = len(matrix)

    # Iterate through each layer of the matrix
    for i in range(n // 2):
        # Calculate the ending index for this layer
        for j in range(i, n - i - 1):
            # Save the top element
            temp = matrix[i][j]

            # Move left to top
            matrix[i][j] = matrix[n - 1 - j][i]

            # Move bottom to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # Move right to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # Move top to right
            matrix[j][n - 1 - i] = temp


# Example usage
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
