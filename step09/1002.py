# 1002.py

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    add = (r1 + r2) ** 2
    sub = (r1 - r2) ** 2
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance > add or distance < sub:
        print(0)
    elif distance == add or distance == sub:
        print(1)
    else:
        print(2)