#!/usr/bin/python3

def weight_average(my_list=[]):
    """Example"""
    """input = [(1, 2), (2, 1), (3, 10), (4, 2)]"""
    """left_operation = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2))"""
    """right_operation = (2 + 1 + 10 + 2)"""
    """output = left_operation / right_operation"""

    """Solution"""
    left_operation, right_operation, output = 0, 0, 0
    n = len(my_list)
    if not my_list:
        return output
    else:
        for index in range(0, n):
            left_operation += my_list[index][0] * my_list[index][1]
            right_operation += my_list[index][1]
        output = left_operation / right_operation
        return output
