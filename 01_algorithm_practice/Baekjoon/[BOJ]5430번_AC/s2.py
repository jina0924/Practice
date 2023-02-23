# 백준 5430번 AC

import sys
sys.stdin = open('input1.txt')
from collections import deque

T = int(input())

for tc in range(T):
    p = input()
    n = int(input())
    data = input()
    if len(data) > 2:
        nums = deque(data[1:-1].split(','))
    else:
        nums = []
    cnt = 0
    isEnd = False
    for i in range(len(p)):
        if p[i] == 'R':
            cnt += 1
        else:
            if not len(nums):
                print('error')
                isEnd = True
                break
            else:
                if cnt % 2:
                    nums.pop()
                else:
                    nums.popleft()
    if not isEnd:
        if cnt % 2:
            nums.reverse()
        print('[', ','.join(nums), ']', sep='')
