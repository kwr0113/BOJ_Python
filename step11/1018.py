# 1018.py

def re_bboard(mboard, x, y):
    cnt = 0
    board = ['BWBWBWBW', 'WBWBWBWB'] * 4
    for i in range(8):
        for j in range(8):
            if mboard[x + i][y + j] != board[i][j]:
                cnt += 1
    return cnt


def re_wboard(mboard, x, y):
    cnt = 0
    board = ['WBWBWBWB', 'BWBWBWBW'] * 4
    for i in range(8):
        for j in range(8):
            if mboard[x + i][y + j] != board[i][j]:
                cnt += 1
    return cnt


n, m = map(int, input().split())
myboard = [input() for _ in range(n)]
mincnt = []

for i in range(n - 7):
    for j in range(m - 7):
        mincnt.append(re_wboard(myboard, i, j))
        mincnt.append(re_bboard(myboard, i, j))

print(min(mincnt))
