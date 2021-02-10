# 2839.py

n = int(input())

s5 = n // 5
s3 = (n % 5) // 3
while (s5 * 5) + (s3 * 3) != n:
    s5 -= 1
    if s5 < 0:
        s3 = 0
        break
    s3 = (n - (s5 * 5)) // 3
print(s5 + s3)