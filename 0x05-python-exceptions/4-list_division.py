#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    number = 0
    result = []
    for number in range(list_length):
        try:
            res = (my_list_1[number]/my_list_2[number])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            number += 1
            result.append(res)
    return result
