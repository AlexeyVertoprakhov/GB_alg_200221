a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


def residual(a, b):
    if b == 0:
        return a
    return residual(a - 1, b - 1)


def product(a, b):
    if (a < b):
        return product(b, a)
    elif b != 0:
        return (a + product(a, b - 1))
    else:
        return 0


def remaind(a, b):
    return remaind(a / b, b) if a >= b else a


print("Сумма двух чисел равна : ", sum(a, b))
print("Разность двух чисел равна : ", residual(a, b))
print("Произведение двух чисел будет : ", product(a, b))
print("Частное двух чисел будет : ", remaind(a, b))
