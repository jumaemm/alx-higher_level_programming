#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    counter = 0
    for c in str:
        if (counter != n):
            new_string += c
        counter += 1
    return new_string
