# 1929-1.py

m, n = map(int, input().split())


def is_prime(a):
    if a == 1:
        return False
    for j in range(2, int(pow(a, 0.5)+1)):
        if a % j == 0:
            return False
    return True


for i in range(m, n+1):
    if is_prime(i):
        print(i)