# 14888.py

import itertools


def expr(ope, num):
    idx = 0
    total = num[idx]
    for i in ope:
        if i == '+':
            total = total + num[idx+1]
        elif i == '-':
            total = total - num[idx+1]
        elif i == '*':
            total = total * num[idx+1]
        elif i == '/':
            if total < 0:
                total = (abs(total) // num[idx+1]) * -1
            else:
                total = total // num[idx+1]
        idx += 1
    return total


n = int(input())
nums = list(map(int, input().split()))
op1 = list(map(int, input().split()))

op2 = '+' * op1[0] + '-' * op1[1] + '*' * op1[2] + '/' * op1[3]
operator = set(itertools.permutations(op2, n - 1))
operator = list(operator)
operator.sort()

result = []
for i in operator:
    result.append(expr(i, nums))

print(max(result))
print(min(result))
