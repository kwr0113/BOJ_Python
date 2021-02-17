# 2447-2.py

def blank(arrays, x, y, n):
    for i in range(int(x), int(x + n)):
        for j in range(int(y), int(y + n)):
            arrays[i][j] = ' '


def star(arrays, x, y, n):
    if n == 1:
        return
    n /= 3
    blank(arrays, x + n, y + n, n)
    for i in range(3):
        for j in range(3):
            star(arrays, x + n * i, y + n * j, n)


a = int(input())
array = [['*' for i in range(a)] for i in range(a)]

star(array, 0, 0, a)

for i in range(a):
    for j in range(a):
        print(array[i][j], end='')
    print()
