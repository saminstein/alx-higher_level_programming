#!/usr/bin/python3

def element_at(my_list, idx):
    """
    fuction that retrieves an element from a list like in c

    Args:
        my_list: The list
        idx: The index of the element to retrieve

    Returns:
        if idx is negative return none, if idx is out of range return none

    """
    list_len = len(my_list)

    if idx in range(list_len):
        element = my_list[idx]
        return element
    else:
        return None