#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()
        number = len(lines)
        if nb_lines <= 0 or nb_lines >= number:
            for line in lines:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(lines[i], end='')
