def first(a):
    if a == 1:
        return a
    elif a > 0:
        return a + first(a - 1)


def second(b):
    return b * (b + 1) // 2


n = 1

while True:
    if first(n) == second(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1
