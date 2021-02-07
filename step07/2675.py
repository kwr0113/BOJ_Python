# 2675.py

n = int(input())

for i in range(n):
    num, s = input().split()
    num = int(num)
    ss = ''
    for j in s:
        ss += j * num
    print(ss)