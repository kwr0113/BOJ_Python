# 1912.py

n = int(input())
num = [i for i in map(int, input().split())]

for i in range(1, n):
    num[i] = max(num[i], num[i] + num[i-1])

print(max(num))
