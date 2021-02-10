# 2775.py

n = int(input())

for _ in range(n):
    k = int(input())
    n = int(input())
    f = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            f[j] = f[j-1] + f[j]
    print(f[n-1])