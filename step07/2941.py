# 2941.py

s = input()
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in l:
    s = s.replace(i, '#')

print(len(s))