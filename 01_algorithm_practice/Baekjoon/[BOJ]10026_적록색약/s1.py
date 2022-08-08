# 백준 10026번 적록색약

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def bfs(r, c):
    global cnt1
    queue = [(r, c)]

    while queue:
        cr, cc = queue.pop()
        color = data[cr][cc]
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if data[nr][nc] == color:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    cnt1 += 1


N = int(input())
data = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt1, cnt2 = 0, 0
RG = True
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            visited[r][c] = 1
            bfs(r, c)
            if data[r][c] == 'B':
                cnt2 += 1
                RG = False
            else:
                RG = True
print(f'{cnt1} {cnt2}')