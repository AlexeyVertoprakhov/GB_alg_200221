"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

n = 0
i = range(2, 100)
for a in i:
    print(a, end=" ")
print()
j = range(2, 10)
for b in j:
    print(b, end=" ")
print()
for x in j:
    for y in i:
        if y % x == 0:
            n += 1
list_1 = list(range(n))
print("Количество кратных чисел = " + str(list_1[-1:]))

'''
not good
arr_1 = []
for i in range(2, 99):
    arr_1.append(i)
    print(arr_1)
    for n in range(j, g):
        if n % j == 0:
'''
