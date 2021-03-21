"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
меньше медианы, в другой — не больше медианы.
"""
from random import randint


def median(list_2, mid):
    right = []
    left = []
    f_n = []                        # find_number искомое число, "медиана"
    for i in list_2:
        if i < mid:
            right.append(i)  # справа от 'середины' middle
        if i > mid:
            left.append(i)  # слева от 'середины' middle
        else:
            f_n.append(i)

    return f_n, right, left


N = 20
list_1 = [randint(10, 100) for i in range(N)]
print(list_1)
list_2 = sorted(list_1)  # сортируем список и добавляем в новый list-2
print(list_2)
print("median")

# firstly variant мне не было понятно почему, значение медианы не выводилось на экран, в принте оставил только текст.
