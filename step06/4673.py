# 4673.py

def d(n):
    return n + sum(map(int, str(n)))

sNum = set()

for i in range(1, 10001):
    a = d(i)
    if a < 10001:
        sNum.add(a)

for i in range(1, 10001):
    if i not in sNum:
        print(i)