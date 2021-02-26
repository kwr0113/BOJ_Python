# 2156.PY

n = int(input())

grape = [int(input()) for _ in range(n)]
t_grape = [0 for _ in range(n)]

t_grape[0] = grape[0]

if n > 1:
    t_grape[1] = grape[0] + grape[1]
if n > 2:
    t_grape[2] = grape[2] + max(grape[0], grape[1])

for i in range(3, n):
    t_grape[i] = grape[i] + max(t_grape[i-2], grape[i-1] + t_grape[i-3], grape[i-1] + t_grape[i-4])

print(max(t_grape))
