# 4153.py

while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break

    a = sorted(a)
    if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print('right')
    else:
        print('wrong')