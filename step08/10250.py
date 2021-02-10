# 10250.py

n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())
    if n % h != 0:
        a = (n % h) * 100 + (n // h) + 1
    else:
        a = h * 100 + (n // h)
    print(a)

