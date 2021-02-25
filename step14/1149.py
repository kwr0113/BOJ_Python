# 1149.py

n = int(input())

house = [[0] * 3 for i in range(n)]
for i in range(n):
    house[i][0], house[i][1], house[i][2] = map(int, input().split())

for i in range(1, n):
    house[i][0] = house[i][0] + min(house[i-1][1], house[i-1][2])
    house[i][1] = house[i][1] + min(house[i-1][0], house[i-1][2])
    house[i][2] = house[i][2] + min(house[i-1][0], house[i-1][1])

print(min(house[n-1]))