# 1978-2.py

n = int(input())
a = list(map(int, input().split()))
count = n
for i in a:
    if i == 1:
        count -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            count -= 1
            break

print(count)