# 1978-1.py

n = int(input())
count = 0
prime = [2, 3]

for i in range(4, 1001):
    pp = [i % k for k in prime]
    if all(pp):
        prime.append(i)

for i in list(map(int, input().split())):
    if i in prime:
        count += 1

print(count)