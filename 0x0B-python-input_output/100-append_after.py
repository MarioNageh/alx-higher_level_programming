#!/usr/bin/python3
"""append after module"""



def append_after(filename="", search_string="", new_string=""):
    """
    Insert a new string of after search string
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
    file.truncate()
