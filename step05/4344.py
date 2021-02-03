# 4344.py

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    avg = (sum(a) - a[0]) / a[0]
    count = 0
    for j in a[1:]:
        if j > avg:
            count += 1
    print("%.3f%%" % ((count / a[0]) * 100))
