#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as af:
        af.write(text)
        num_char = len(text)
        return num_char
