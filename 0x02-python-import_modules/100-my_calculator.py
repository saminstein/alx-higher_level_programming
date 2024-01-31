#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = {'+': add, '-': sub, '*': mul, '/': div}

    num_args = len(argv)
    if num_args != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
