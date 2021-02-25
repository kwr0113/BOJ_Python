# 2579.py

n = int(input())

stair = [int(input()) for _ in range(n)]
cost = [0 for _ in range(n)]

cost[0] = stair[0]

if n > 1:
    cost[1] = stair[1] + stair[0]
if n > 2:
    cost[2] = stair[2] + max(stair[0], stair[1])

for i in range(3, n):
    cost[i] = stair[i] + max(stair[i-1] + cost[i-3], cost[i-2])

print(cost[n-1])
