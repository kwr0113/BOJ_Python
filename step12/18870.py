# 18870.py

num = int(input())
l1 = list(map(int, input().split()))
l2 = sorted(list(set(l1)))

after = {l2[i]: i for i in range(len(l2))}

for i in l1:
    print(after[i], end=' ')