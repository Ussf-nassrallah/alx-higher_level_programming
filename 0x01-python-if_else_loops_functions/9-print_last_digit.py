#!/usr/bin/python3
def print_last_digit(input):
    last_digit = abs(input) % 10
    print("{}".format(last_digit), end="")
    return (last_digit)
