# 1932.py

n = int(input())

tri = [[i for i in map(int, input().split())] for i in range(n)]

for i in range(1, n):
    tri[i][0] = tri[i][0] + tri[i-1][0]
    for j in range(1, i):
        tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])
    tri[i][i] = tri[i][i] + tri[i-1][i-1]

print(max(tri[n-1]))