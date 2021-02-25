# 10844.py

n = int(input())

step = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(1, n):
    n0 = step[i-1][1]
    n1 = step[i-1][0] + step[i-1][2]
    n2 = step[i-1][1] + step[i-1][3]
    n3 = step[i-1][2] + step[i-1][4]
    n4 = step[i-1][3] + step[i-1][5]
    n5 = step[i-1][4] + step[i-1][6]
    n6 = step[i-1][5] + step[i-1][7]
    n7 = step[i-1][6] + step[i-1][8]
    n8 = step[i-1][7] + step[i-1][9]
    n9 = step[i-1][8]
    step.append([n0, n1, n2, n3, n4, n5, n6, n7, n8, n9])

print(sum(step[n-1]) % 1000000000)
