# 1011.py

import math

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    root = math.floor(math.sqrt(distance))

    if distance == math.pow(root, 2):
        print(2 * root - 1)
    elif distance <= math.pow(root, 2) + root:
        print(2 * root)
    else:
        print(2 * root + 1)