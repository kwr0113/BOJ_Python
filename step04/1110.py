# 1110.py

n = int(input())
nn = n
count = 0

while True:
    if nn == n and count != 0:
        break
    a = n // 10
    b = n % 10
    c = a + b
    n = int(str(b) + str(c % 10))
    count += 1

print(count)