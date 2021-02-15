# 4948-2.py

N = 123456 * 2 + 1

prime = [False, False] + [True] * (N - 1)
for i in range(2, int(pow(N, 0.5) + 1)):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):
        if prime[i]:
            count += 1
    print(count)
