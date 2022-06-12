# SWEA 5247. 연산

import sys
sys.stdin = open('input.txt')
from collections import deque


def calc():
    queue = deque([N])
    nums[N] = 1

    while queue:
        num = queue.popleft()
        if num == M:
            return
        if 0 < num+1 <= 1000000 and not nums[num+1]:
            nums[num+1] = nums[num] + 1
            queue.append(num+1)
        if 0 < num - 1 <= 1000000 and not nums[num-1]:
            nums[num-1] = nums[num] + 1
            queue.append(num-1)
        if 0 < num*2 <= 1000000 and not nums[num*2]:
            nums[num*2] = nums[num] + 1
            queue.append(num*2)
        if 0 < num - 10 <= 1000000 and not nums[num-10]:
            nums[num-10] = nums[num] + 1
            queue.append(num-10)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = [0] * 1000001
    calc()
    print(f'#{tc} {nums[M] - 1}')