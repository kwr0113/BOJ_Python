# 4948-1.py

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    prime = [False, False] + [True] * (2*n - 1)
    for i in range(2, int(pow(2*n, 0.5) + 1)):
        if prime[i]:
            for j in range(i * i, 2*n + 1, i):
                prime[j] = False

    for i in range(n+1, 2*n+1):
        if prime[i]:
            count += 1
    print(count)
