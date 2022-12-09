#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    square = [[x**2 for x in y] for y in matrix_copy]
    return square
