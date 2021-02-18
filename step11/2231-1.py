# 2231-1.py

def add(x):
    a = list(map(int, str(x)))
    return x + sum(a)


n = int(input())
t = 0
i = 0
while n != t:
    if i >= 1000000:
        i = 0
        break
    i += 1
    t = add(i)

print(i)