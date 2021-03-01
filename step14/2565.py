# 2565.py

num = int(input())
wire = [[i for i in map(int, input().split())] for _ in range(num)]
wire.sort()

seq = [i[1] for i in wire]
t_seq = [1] + [0 for _ in range(num-1)]

for i in range(1, num):
    a = [0]
    for j in range(i):
        if seq[j] < seq[i]:
            a.append(t_seq[j])
    t_seq[i] = max(a) + 1

print(num - max(t_seq))