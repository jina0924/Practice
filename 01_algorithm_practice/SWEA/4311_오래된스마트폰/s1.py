# SWEA 4311. 오래된 스마트폰

import sys
sys.stdin = open('input.txt')
from collections import deque


def touch():
    queue = deque([])
    for num in nums:
        queue.append((num, 1))

    while queue:
        num, cnt = queue.popleft()
        for i in range(N):
            nnum = num * 10 + nums[i]
            if cnt + 1 <= M and nnum <= 999:
                if nnum == W:
                    return cnt + 1
                else:
                    queue.append((nnum, cnt + 1))
        for o in range(O):
            for i in range(N):
                if opers[o] == 1:
                    nnum = num + nums[i]
                elif opers[o] == 2:
                    nnum = num - nums[i]
                elif opers[o] == 3:
                    nnum = num * nums[i]
                elif opers[o] == 4:
                    if nums[i] == 0:
                        continue
                    else:
                        nnum = num // nums[i]
                if cnt + 2 <= M and 0 <= nnum <= 999:
                    if nnum == W:
                        return cnt + 3
                    else:
                        queue.append((nnum, cnt + 2))

    return -1


T = int(input())

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    W = int(input())
    print(f'#{tc} {touch()}')