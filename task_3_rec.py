def rec(a, i):
    return i if (a == 0) else rec(a // 10, i * 10 + a % 10)


print(rec(int(input("Введите любое целое число : ")), 0))
