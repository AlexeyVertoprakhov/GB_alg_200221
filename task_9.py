"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
"""

number = int(input("Введите натуральные числа, для оставки ввода и вывода результата, введите '0': "))
max_sum = 0
max_digit = 0
while number != 0:
    m_d = number
    m_s = 0
    while number > 0:
        m_s += number % 10
        number //= 10
    if m_s > max_sum:
        max_sum = m_s
        max_digit = m_d
    number = int(input())
print('Число', max_digit, 'имеет максимальную сумму цифр:', max_sum)
