# 백준 10026번 적록색약

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(r, c, visited):
    queue = [(r, c)]
    color = data[r][c]

    while queue:
        cr, cc = queue.pop()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if data[nr][nc] == color:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    return 1


N = int(input())
data = [list(input().rstrip()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt1, cnt2 = 0, 0
for r in range(N):
    for c in range(N):
        if not visited1[r][c]:
            visited1[r][c] = 1
            cnt1 += bfs(r, c, visited1)
        elif not visited2[r][c]:
            visited2[r][c] = 1
            cnt2 += bfs(r, c, visited2)
print(f'{cnt1} {cnt2}')