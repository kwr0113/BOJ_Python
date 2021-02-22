# 1003.py

n = int(input())

fibo0 = [1, 0]
fibo1 = [0, 1]

for i in range(39):
    fibo0.append(fibo0[i] + fibo0[i+1])
    fibo1.append(fibo1[i] + fibo1[i + 1])

for _ in range(n):
    num = int(input())
    print(fibo0[num], fibo1[num])