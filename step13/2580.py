# 2580.py

def check(x, y, num):
    ch_row = sudoku[x]
    ch_col = [sudoku[i][y] for i in range(9)]
    a = (x // 3) * 3
    b = (y // 3) * 3
    ch_block = sudoku[a][b:b + 3] + sudoku[a + 1][b:b + 3] + sudoku[a + 2][b:b + 3]
    if num in ch_row:
        return False
    elif num in ch_col:
        return False
    elif num in ch_block:
        return False
    else:
        return True


def sdk(zeros):
    if not zeros:
        for i in sudoku:
            print(' '.join(map(str, i)))
        return

    for t in range(1, 10):
        i, j = zeros.pop()
        if check(i, j, str(t)):
            sudoku[i][j] = str(t)
            sdk(zeros)
            sudoku[i][j] = '0'
        zeros.append([i, j])


sudoku = [[str(i) for i in input().split()] for _ in range(9)]
myzeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == '0']
sdk(myzeros)