#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in range(0, len(matrix)):
        for cols in range(0, len(matrix[rows])):
            if cols != 0:
                print(" ", end="")
            print("{:d}".format(matrix[rows][cols]), end="")

        print()