#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    for k, v in sorted(a_dic.items()):
        print("{}: {}".format(k, v))
