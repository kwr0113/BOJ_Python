# 11053.py

n = int(input())
seq = [i for i in map(int, input().split())]
t_seq = [1] + [0 for _ in range(n-1)]

for i in range(1, n):
    a = [0]
    for j in range(i):
        if seq[j] < seq[i]:
            a.append(t_seq[j])
    t_seq[i] = max(a) + 1

print(max(t_seq))