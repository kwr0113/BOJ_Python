# 2581-2.py

m = int(input())
n = int(input())
mn = []


def is_prime(a):
    if a == 1:
        return False
    for j in range(2, a):
        if a % j == 0:
            return False
    return True


for i in range(m, n+1):
    if is_prime(i):
        mn.append(i)

if not mn:
    print(-1)
else:
    print(sum(mn))
    print(min(mn))