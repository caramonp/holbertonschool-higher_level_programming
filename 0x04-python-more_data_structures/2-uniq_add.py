#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = []
    suma = 0
    for i in my_list:
        if i not in total:
            total.append(i)
    for c in total:
        suma += c
    return suma
