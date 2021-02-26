# 11054.py

n = int(input())
seq_1 = [i for i in map(int, input().split())]
t_seq_1 = [1] + [0 for _ in range(n-1)]
seq_2 = [i for i in seq_1]
seq_2.reverse()
t_seq_2 = [1] + [0 for _ in range(n-1)]

for i in range(1, n):
    a = [0]
    b = [0]
    for j in range(i):
        if seq_1[j] < seq_1[i]:
            a.append(t_seq_1[j])
        if seq_2[j] < seq_2[i]:
            b.append(t_seq_2[j])
    t_seq_1[i] = max(a) + 1
    t_seq_2[i] = max(b) + 1

t_seq_2.reverse()
t_seq = [t_seq_1[i] + t_seq_2[i] - 1 for i in range(n)]
print(max(t_seq))
