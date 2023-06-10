#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        for child_list in inner_list:
            print("{:d}".format(child_list), end=" ")
        print()
