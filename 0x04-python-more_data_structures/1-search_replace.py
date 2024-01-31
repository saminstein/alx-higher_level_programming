#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for elems in my_list:
        if elems == search:
            new_list.append(replace)
        else:
            new_list.append(elems)

    return new_list
