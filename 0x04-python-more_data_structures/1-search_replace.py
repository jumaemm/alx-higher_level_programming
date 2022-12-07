#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = [x if x != search else replace for x in my_list]
    return list2
