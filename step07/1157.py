# 1157.py

s = input().upper()
alphabet = [0 for i in range(26)]

for i in s:
    alphabet[ord(i)-65] += 1

m = max(alphabet)
idx = alphabet.index(m)

if alphabet.count(m) > 1:
    print('?')
else:
    print(chr(idx+65))

