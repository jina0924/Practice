# 백준 14395번 4연산 - 시간초

import sys
sys.stdin = open('input.txt')

s, t = map(int, input().split())
if s == t:
    print(0)
    sys.exit()
elif t % 2 and t != 1:
    print(-1)
    sys.exit()
nums = [(s ** 2, '*'), (s * 2, '+'), (0, '-'), (1, '/')]
for num, operators in nums:
    if num == t:
        print(operators)
        break
    else:
        nums.append((num ** 2, operators + '*'))
        nums.append((num * 2, operators + '+'))
