"""
6.	Пользователь вводит номер буквы в алфавите. Определить, какая это бук
"""

n = int(input("Введите номер буквы (1 - 26): "))

l_num = ord('a') + n - 1
print("Это номер буквы -- " + chr(l_num))


