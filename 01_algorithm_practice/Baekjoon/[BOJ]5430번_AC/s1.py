# 백준 5430번 AC

import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(T):
    p = input()
    n = int(input())
    data = input()
    nums = deque([])
    idx = 1
    num = ''
    if len(data) > 2:
        while idx < len(data):
            if data[idx] != ',' and data[idx] != ']':
                num += data[idx]
            else:
                nums.append(num)
                num = ''
            idx += 1
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
