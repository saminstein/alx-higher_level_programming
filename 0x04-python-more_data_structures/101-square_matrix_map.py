#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda rows: list(map(
      lambda elem: elem ** 2, rows)), matrix))
    return new_matrix
