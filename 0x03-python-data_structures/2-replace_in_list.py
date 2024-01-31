#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    fuction that replaces an element of a list at a specific position

    Args:
        my_list: The list
        idx: The index of the element to replace
        element: The element to replace with

    Returns:
        if idx is negative return none, if idx is out of range
        return original list
    """

    list_len = len(my_list)

    if 0 <= idx and idx < list_len:
        my_list[idx] = element
        return my_list
    else:
        return my_list
