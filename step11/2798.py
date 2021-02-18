# 2798.py

n, m = map(int, input().split())
card = list(map(int, input().split()))

total = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for l in range(j+1, n):
            a = card[i] + card[j] + card[l]
            if m >= a > total:
                total = a

print(total)