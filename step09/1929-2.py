# 1929-2.py

m, n = map(int, input().split())
prime = [False, False] + [True] * (n - 1)
for i in range(2, int(pow(n, 0.5)+1)):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if prime[i]:
        print(i)