# 2447.py

def divstar(arrays, x, y, n):
    star(arrays, x, y, n / 3)
    star(arrays, x, y + n / 3, n / 3)
    star(arrays, x, y + 2 * n / 3, n / 3)
    star(arrays, x + n / 3, y, n / 3)
    blank(arrays, x + n / 3, y + n / 3, n / 3)
    star(arrays, x + n / 3, y + 2 * n / 3, n / 3)
    star(arrays, x + 2 * n / 3, y, n / 3)
    star(arrays, x + 2 * n / 3, y + n / 3, n / 3)
    star(arrays, x + 2 * n / 3, y + 2 * n / 3, n / 3)


def blank(arrays, x, y, n):
    for i in range(int(x), int(x + n)):
        for j in range(int(y), int(y + n)):
            arrays[i][j] = ' '


def star(arrays, x, y, n):
    if n == 1:
        return

    divstar(arrays, x, y, n)


a = int(input())
array = [['*' for i in range(a)] for i in range(a)]

divstar(array, 0, 0, a)

for i in range(a):
    for j in range(a):
        print(array[i][j], end='')
    print()
