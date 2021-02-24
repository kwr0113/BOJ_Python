# 9461.py

t = int(input())
wave = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(t):
    n = int(input())
    if n <= len(wave) - 1:
        print(wave[n])
    else:
        for l in range(len(wave), n+1):
            wave.append(wave[l-1] + wave[l-5])
        print(wave[n])

