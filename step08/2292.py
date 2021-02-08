# 2292.py

n = int(input())
i, num = 1, 1
while n > num:
    num = num + (6 * i)
    i += 1
print(i)