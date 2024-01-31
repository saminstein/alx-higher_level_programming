#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """
    prints the result of the addition of all arguments
    """

num_args = len(sys.argv)

if num_args == 1:
    print("0")
elif num_args >= 3:
    total = 0
    for args in sys.argv[1:]:
        total += int(args)

    print(f"{total}")
