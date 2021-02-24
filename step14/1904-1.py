# 1904-1.py

n = int(input())
array = [0, 1, 2] + [0] * n

for i in range(3, n+1):
    array[i] = (array[i-1] + array[i-2]) % 15746

print(array[n])
