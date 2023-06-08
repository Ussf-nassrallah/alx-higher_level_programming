#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul

    a = 10
    b = 5
    sum = add(a, b)
    product = mul(a, b)
    diff = sub(a, b)
    div_result = div(a, b)

    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, div_result))
