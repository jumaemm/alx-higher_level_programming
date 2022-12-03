#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """List idex out of range"""
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    list_copy = [elem for elem in my_list]
    list_copy[idx] = element
    return list_copy
