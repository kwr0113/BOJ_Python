# 1463.py

n = int(input())

num = [0, 0, 1, 1] + [0 for _ in range(n-3)]

for i in range(4, n+1):
    num[i] = num[i-1] + 1
    if i % 3 == 0:
        num[i] = min(num[i], num[i//3] + 1)
    if i % 2 == 0:
        num[i] = min(num[i], num[i//2] + 1)

print(num[n])
