# 9184.py

import sys

ww = [[[0] * 21 for _ in range(21)] for __ in range(21)]


def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)
    if ww[x][y][z]:
        return ww[x][y][z]
    if x < y < z:
        ww[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
        return ww[x][y][z]
    ww[x][y][z] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
    return ww[x][y][z]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

