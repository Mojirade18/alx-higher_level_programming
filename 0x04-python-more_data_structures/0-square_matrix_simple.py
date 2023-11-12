#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
    - matrix: 2-dimensional list (matrix of integers)

    Returns:
    - New matrix with each value squared
    """
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)

    # Print the new matrix and the original matrix to verify that the original matrix is not modified
    print(new_matrix)
    print(matrix)
