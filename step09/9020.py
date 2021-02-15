# 9020.py

N = 10001

prime = [False, False] + [True] * (N - 1)
for i in range(2, int(pow(N, 0.5) + 1)):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

t = int(input())

for i in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
