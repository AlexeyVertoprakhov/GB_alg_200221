"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random

# согласно урока на убывание заменил 1 на n, поскольку имеется предварительное условие в виде переменной n.

array = []


for i in range(10):
    numbers = (int(random.randint(-100, 99)))
    array.append(numbers)
    print(array)
    print()


n = 1
while n < len(array):
    is_sorted = True
    for i in range(len(array) - n):
        if array[i] > array[i - n]:
            array[i], array[i - n] = array[i - n], array[i]
            is_sorted = False

    if is_sorted:
        break

    n += 1
    print(array)


"""
# класический из книжки по возрастанию

def bubble_sort(nums):  

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) + 1):
            if nums[i] > nums[i + 1]:

                nums[i], nums[i + 1] = nums[i + 1], nums[i]
               
                swapped = True


array = []


for i in range(10):
    numbers = (int(random.randint(-100, 99)))
    array.append(numbers)
    print(array)
    print()

random_list_of_nums = array
bubble_sort(random_list_of_nums)  
print(random_list_of_nums)

"""


