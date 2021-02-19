# 2108.py

import collections
import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()

modea = collections.Counter(a).most_common()
maxinum = modea[0][0]
try:
    if modea[1][1] == modea[0][1]:
        maxinum = modea[1][0]
except:
    pass

print(round(sum(a)/n))
print(a[n//2])
print(maxinum)
print(a[n-1] - a[0])