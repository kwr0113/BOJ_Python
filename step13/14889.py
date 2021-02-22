# 14889.py

import itertools


def t_status(t):
    total = 0
    for i in t:
        for j in t:
            s = status[i-1][j-1]
            total += s
    return total


n = int(input())
p = [i for i in range(1, n+1)]
status = [[i for i in map(int, input().split())] for _ in range(n)]

team = list(itertools.combinations(p, n//2))

team_status = [t_status(i) for i in team]
team_status_gap = [abs(team_status[i] - team_status[-1-i]) for i in range(len(team)//2)]

print(min(team_status_gap))


