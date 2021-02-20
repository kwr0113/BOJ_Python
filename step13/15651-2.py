# 15651-2.py

def sequence(seq, n, m):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, n+1):
        seq.append(i)
        sequence(seq, n, m)
        seq.pop()


n, m = map(int, input().split())
nm = []
sequence(nm, n, m)