# 11651.py

import sys

n = int(input())
xy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
xy = sorted(xy, key=lambda t: (t[1], t[0]))
for i in xy:
    print(i[0], i[1])