# 2581-1.py

m = int(input())
n = int(input())
mn = []

prime = [2, 3]
for i in range(4, 10001):
    pp = [i % k for k in prime]
    if all(pp):
        prime.append(i)

for i in range(m, n+1):
    if i in prime:
        mn.append(i)

if not mn:
    print(-1)
else:
    print(sum(mn))
    print(min(mn))