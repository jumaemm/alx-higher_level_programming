#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_num = 0
    max_key = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_num:
            max_num = a_dictionary[key]
            max_key = key
        else:
            continue
    return max_key
