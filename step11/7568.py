# 7568.py

n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split())))

for mh, mw in people:
    count = 1
    for yh, yw in people:
        if mh < yh and mw < yw:
            count += 1
    print(count, end=' ')
