#!/usr/bin/python3
"""append after module"""


def append_after(filename="", search_string="", new_string=""):
    '''module Search and update
    '''
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
                f.write('\n')
