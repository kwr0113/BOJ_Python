# 11729.py

def hanoi(n, start, middle, goal):
    if n == 1:
        print(f'{start} {goal}')
    else:
        hanoi(n-1, start, goal, middle)
        print(f'{start} {goal}')
        hanoi(n-1, middle, start, goal)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)