#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        matrix = []
    new_matrix = []

    for rows in matrix:
        new_row = list(map(lambda x: x ** 2, rows))
        new_matrix.append(new_row)
    return new_matrix
