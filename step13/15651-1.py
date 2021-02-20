# 15651-1.py

def sequence(seq, n, m, index):
    for i in range(1, n+1):
        seq[index] = i
        if index + 1 == m:
            print(' '.join(map(str, seq)))
        else:
            sequence(seq, n, m, index+1)


n, m = map(int, input().split())
nm = [0 for _ in range(m)]
sequence(nm, n, m, 0)