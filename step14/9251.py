# 9251.py

s1 = str(input())
s2 = str(input())

s1s2 = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            s1s2[i][j] = s1s2[i-1][j-1] + 1
        else:
            s1s2[i][j] = max(s1s2[i-1][j], s1s2[i][j-1])

print(s1s2[i][j])
