# 2231-2.py

def add(x):
    a = list(map(int, str(x)))
    return x + sum(a)


n = int(input())
t = 0

for i in range(1, n+1):
    if n == add(i):
        t = i
        break

print(t)