#!/usr/bin/env python3

def no_c(my_string):
    result_str = " "

    for char in my_string:
        if char != 'c' and char != 'C':
            continue
        result_str += char

    return result_str
