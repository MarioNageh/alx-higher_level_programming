#!/usr/bin/python3
def print_last_digit(nm):
    if nm < 0:
        l_dig = nm % -(10)
        print(-(l_dig), end='')
    else:
        l_dig = nm % 10
        print(l_dig, end='')
    return abs(l_dig)
