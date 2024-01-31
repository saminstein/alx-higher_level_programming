#!/usr/bin/python3

def roman_to_int(r_str):
    r_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
      }

    if r_str is None or type(r_str) is not str:
        return 0

    result = 0
    for i in range(0, len(r_str)):
        value = r_numerals[r_str[i]]

        if i + 1 < len(r_str) and r_numerals[r_str[i + 1]] > value:
            result -= value
        else:
            result += value
        return result
