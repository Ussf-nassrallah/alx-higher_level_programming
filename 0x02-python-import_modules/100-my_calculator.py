#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arguments = sys.argv
    arguments_count = len(arguments)
    oper_list = ['+', '-', '*', '/']

    if (arguments_count - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(arguments[1])
    oper = arguments[2]
    b = int(arguments[3])

    if oper not in list(oper_list):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif oper == oper_list[0]:
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif oper == oper_list[1]:
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif oper == oper_list[2]:
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
