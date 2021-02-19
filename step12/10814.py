# 10814.py

import sys

n = int(sys.stdin.readline())
member = [list(sys.stdin.readline().split()) for _ in range(n)]
member = sorted(member, key=lambda t: int(t[0]))
for i in member:
    print(i[0], i[1])