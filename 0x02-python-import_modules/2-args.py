#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv
    arguments_count = len(arguments)

    if arguments_count == 1:
        print("{} arguments.".format(arguments_count - 1))
    elif arguments_count == 2:
        print("{} argument:".format(arguments_count - 1))
        print("{}: {}".format(arguments_count - 1, arguments[1]))
    else:
        print("{} arguments:".format(arguments_count - 1))
        for index in range(1, arguments_count):
            print("{}: {}".format(index, arguments[index]))
