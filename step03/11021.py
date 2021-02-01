# 11021.py

n = int(input())

for i in range(1, n+1):
    n, m = map(int, input().split())
    print("Case #" + str(i) + ":", str(n + m))