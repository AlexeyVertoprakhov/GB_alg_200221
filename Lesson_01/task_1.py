"""
https://drive.google.com/file/d/1RjnTxor0bUND_ZlI2EMnlS_3wDBbp2pw/view?usp=sharing
1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""

number = int(input("Введите любое трехзначное число: "))
print(f'{number = }')

a = number // 100
b = (number // 10) % 10
c = number % 10

d = a + b + c
e = a * b * c

print("Сумма трех цифр вашего числа = " + str(d))
print("Произведение трех цифр вашего числа = " + str(e))
