# 1065.py

def d(num):
    count = num
    if num < 100:
        return num
    else:
        for i in range(100, num+1):
            a = str(i)
            m = int(a[0]) - int(a[1])
            for j in range(len(a)-1):
                if (int(a[j]) - int(a[j + 1])) != m:
                    count -= 1
                    break
        return count

n = int(input())
print(d(n))
