"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import sys
import collections
from collections import defaultdict
import functools


def calc():
    global sum
    nums = collections.defaultdict(list)
    for d in range(2):
        n = input(f"Введите число {d + 1} - натуральное шестнадцатеричное число: ")
        nums[f"{d + 1}-{n}"] = list(n)
    print(nums)

    sum = sum([int(''.join(i), 16) for i in nums.values()])
    print("Сумма чисел = ", list('XX' % sum))

    mult = functools.reduсe(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print("Произведение чисел = ", list('%X' % mult))


calc()
