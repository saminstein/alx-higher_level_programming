#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list)

    if 0 <= idx and idx < list_len:
        my_list2 = my_list[:]
        my_list2[idx] = element
        return my_list2
    else:
        return my_list
