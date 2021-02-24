# 1904-2.py

n = int(input())
a, b = 1, 2

for _ in range(n-1):
    a, b = b, (a + b) % 15746

print(a)
