# SWEA 5247. 연산

import sys
from collections import deque
sys.stdin = open('input.txt')


def calc():
    queue = deque([N])
    visited[N] = 1

    while queue:
        num = queue.popleft()
        if num == M:
            return
        nums = (num+1, num-1, num*2, num-10)
        for n in nums:
            if 0 < n <= 1000000 and not visited[n]:
                visited[n] = visited[num] + 1
                queue.append(n)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    calc()
    print(f'#{tc} {visited[M] - 1}')