# 1546.py

n = int(input())
score = list(map(int, input().split()))
maxscore = max(score)

nscore = [i * 100 / maxscore for i in score]

print(sum(nscore) / len(nscore))