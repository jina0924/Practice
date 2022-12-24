# 백준 14502번 연구소

import sys
from copy import deepcopy
sys.stdin = open('input3.txt')


def wall(cnt, cr, cc):
    global ans
    if cnt >= 3:
        result = bfs()
        if result > ans:
            ans = result
    else:
        for r in range(N):
            for c in range(M):
                if data[r][c] == 0 and (r > cr or c >= cc):
                    data[r][c] = 1
                    wall(cnt + 1, r, c)
                    data[r][c] = 0


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    lab = deepcopy(data)
    queue = deepcopy(virus)

    while queue:
        cr, cc = queue.pop(0)
        lab[cr][cc] = 2
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not lab[nr][nc]:
                queue.append((nr, nc))
                lab[nr][nc] = 2

    total = 0
    for r in range(N):
        for c in range(M):
            if not lab[r][c]:
                total += 1
    return total


N, M = map(int, input().split())
data = []
virus = []
# visited = [[0] * M for _ in range(N)]
ans = 0
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(M):
        if row[c] == 2:
            virus.append((r, c))
    data.append(row)
wall(0, 0, 0)
print(ans)