#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_of_divisons = []
    for i in range(list_length):
        val = 0
        try:
            val = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as error:
            print("division by 0")
        except TypeError as error:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            list_of_divisons.append(val)
    return list_of_divisons
