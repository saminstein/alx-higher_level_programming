#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """
    function that does some maths and prints the result
    """

    a = 10
    b = 5

    add = add(a, b)
    print("{} + {} = {}".format(a, b, add))

    sub = sub(a, b)
    print("{} - {} = {}".format(a, b, sub))

    mul = mul(a, b)
    print("{} * {} = {}".format(a, b, mul))

    div = div(a, b)
    print("{} / {} = {}".format(a, b, div))
