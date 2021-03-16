"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего
"""
'''
import collections
вариант не совсем рабочий

def calc():
    n = int(input("Введите количество компаний: "))
    d = dict()
    a = 1

    for i in range(n):
        name = input("Введите имя компании: "),
        prof_company = input("Введите прибыль компании за каждый квартал через пробел:\n")
        profit = prof_company.split(" ")
        a += 1
        print()
        fab = collections.Counter(d)

        b = 0
        t = 0
        for i in fab:
            sum = 0
            for j in fab[i]:
                sum += int(j)
                fab[i] = sum
                t += sum
                b += 1
                sec = t / b
                print("Средняя прибыль всех компаний = " + str(sec))
                bigger = []
                smaller = []
                for i in fab:
                    if int(fab[i]) < sec:
                        smaller.append(i)
                        print(smaller)
                    else:
                        bigger.append(i)
                        print(bigger)


calc()
'''
# работает

from collections import namedtuple


def calc():
    my_var = "Company"
    n = int(input("Введите количество компаний: "))
    companies = namedtuple(
        my_var,
        "name period_1 period_2 period_3 period_4")
    profit_aver = {}

    for i in range(n):
        company = companies(
            name=input("Введите название компании: "), period_1=int(
                input("Введите прибыль за I квартал: ")), period_2=int(
                input("Введите прибыль за II квартал:")), period_3=int(
                input("Введите прибыль за III квартал:")), period_4=int(
                input("Введите прибыль за IV квартал:")))

        profit_aver[company.name] = (
                                            company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n

    for key, value in profit_aver.items():
        if value > total_aver:
            print(f"{key} - Прибыль компании выше среднего.")
        elif value < total_aver:
            print(f"{key} - Прибыль компании меньше среднего.")
        elif value == total_aver:
            print(f"{key}Прибыль компании на среднем уровне")


calc()
