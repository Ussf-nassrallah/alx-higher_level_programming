#!/usr/bin/python3

"""
  function that returns a list of lists of integers
  representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """ represent pascal_triangle function """

    if n <= 0:
        return []

    t = [[1]]

    while len(t) != n:
        last_ele = t[-1]
        helper = [1]

        for index in range(len(last_ele) - 1):
            helper.append(last_ele[index] + last_ele[index + 1])

        helper.append(1)
        t.append(helper)
    return t
