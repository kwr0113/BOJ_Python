# 9663.py

n = int(input())

row = [0] * n
column = [False] * n
leri = [False] * (2 * n - 1)
rile = [False] * (2 * n - 1)
cnt = []


def setQueen(i):
    for j in range(n):
        if not column[j] and not leri[i + j] and not rile[i - j + n - 1]:
            row[i] = j
            if i == n - 1:
                cnt.append(1)
            else:
                column[j] = leri[i + j] = rile[i - j + n - 1] = True
                setQueen(i + 1)
                column[j] = leri[i + j] = rile[i - j + n - 1] = False


setQueen(0)
print(len(cnt))
