#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        if i + j == 17:
            print('89')
        else:
            print("{:d}{:d}".format(i, j), end=', ')
