#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    attribute_names = vars(s1).keys()
    print(attribute_names)