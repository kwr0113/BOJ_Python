# 15651-3.py

import itertools

n, m = map(int, input().split())
nm = [str(i) for i in range(1, n+1)]

a = list(itertools.product(nm, repeat=m))
for i in a:
    print(' '.join(i))