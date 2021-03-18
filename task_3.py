"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import random

list_1 = []
list_2 = []
list_3 = []
x = (int(random() * 11)) / 2

for i in range(20):
    n = int(random() * 11)
    list_1.append(n)

a = list_1[-1]
for j in list_1:
    if j <= x:
        a -= 1
        list_2.append(a)

b = list_1[0]
for y in list_1:
    if y >= x:
        b += 1
        list_3.append(b)

list_4 = list_3 + list_2
print(list_4)

'''
При совпадении чисел, почему то числа помещаются с двух сторон  от максимального числа
'''
