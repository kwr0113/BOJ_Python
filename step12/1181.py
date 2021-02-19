# 1181.py

import sys

n = int(input())
words = list({sys.stdin.readline().strip() for _ in range(n)})
words.sort()
words = sorted(words, key=lambda t: len(t))
for i in words:
    print(i)