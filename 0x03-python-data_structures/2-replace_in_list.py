#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """List index out of range"""
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
