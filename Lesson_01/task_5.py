"""
5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, 
и сколько между ними находится букв.
"""

l1 = input("Введите первую букву: (a - z)__")
l2 = input("Введите вторую букву: ( a - z)__")

n1 = ord(l1) - ord('a') + 1
n2 = ord(l2) - ord('a') + 1

print("Номер первой буквы в алфавите -- " + str(n1))
print("Номер второй буквы в алфавите -- " + str(n2))

c1 = int(ord(l1))
c2 = int(ord(l2))
l_count = ((c1 - c2) + 1) * -1  # не учитываем первую и вторую букву введенные пользователем

print("Количество букв в алфавите между введенными, равно: " + str(l_count))
