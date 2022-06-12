# 백준 7576번 토마토

import sys
sys.stdin = open('input2.txt')
from collections import deque


def ripen():
    ans = 0
    queue = deque([])
    for r in range(N):
        for c in range(M):
            if storage[r][c] == 1:
                queue.append((r, c, 0))

    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    while queue:
        cr, cc, days = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and storage[nr][nc] == 0:
                storage[nr][nc] = 1
                queue.append((nr, nc, days+1))
                if ans < days + 1:
                    ans = days + 1
    for r in range(N):
        for c in range(M):
            if storage[r][c] == 0:
                return -1
    return ans


M, N = map(int, input().split())
storage = [list(map(int, input().split())) for _ in range(N)]
print(ripen())

