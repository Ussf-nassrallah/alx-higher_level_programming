#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv
    arguments_count = len(arguments)
    sum = 0

    for index in range(1, arguments_count):
        num = int(arguments[index])
        sum += num

    print("{}".format(sum))
