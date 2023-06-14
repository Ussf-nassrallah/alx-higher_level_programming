#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n = len(matrix)
    new_list = matrix.copy()
    for index in range(0, n):
        new_list[index] = list(map(lambda x: x**2, new_list[index]))
    return new_list
