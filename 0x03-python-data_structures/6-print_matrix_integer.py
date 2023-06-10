#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        for child_list in inner_list:
            if child_list == inner_list[-1]:
                print("{:d}".format(child_list), end="")
            else:
                print("{:d}".format(child_list), end=" ")
        print()
