#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newList = my_list[0:]
    if idx >= 0 and idx <= len(newList) - 1:
        newList[idx] = element
        return newList
    return my_list
