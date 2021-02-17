# 10872.py

def fac(x):
    if x == 0:
        return 1
    else:
        return x * fac(x-1)


x = int(input())
print(fac(x))