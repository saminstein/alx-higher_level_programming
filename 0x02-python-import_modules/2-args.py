#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """
    program that prints the number of and the list of its argumments
    """

    argv = sys.argv
    num_args = len(argv) - 1

    if num_args == 1:
        print(num_args, " arguments")
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))

    elif num_args > 1:
        print(num_args, "arguments")
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))

    elif num_args == 0:
        print(num_args, "arguments")
