# 백준 10026번 적록색약

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def RGB(r, c):
    queue = [(r, c)]
    visited1[r][c] = 1

    while queue:
        cr, cc = queue.pop(0)
        color = drawing[cr][cc]
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and drawing[nr][nc] == color and not visited1[nr][nc]:
                queue.append((nr, nc))
                visited1[nr][nc] = 1
    return 1


def RRB(r, c):
    queue = [(r, c)]
    visited2[r][c] = 1
    isBlue = False
    if drawing[r][c] == 'B':
        isBlue = True

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and isBlue == (drawing[nr][nc] == 'B') and not visited2[nr][nc]:
                queue.append((nr, nc))
                visited2[nr][nc] = 1
    return 1


N = int(input())
drawing = [list(input().rstrip()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
cnt1, cnt2 = 0, 0
for r in range(N):
    for c in range(N):
        if not visited1[r][c]:
            cnt1 += RGB(r, c)
        if not visited2[r][c]:
            cnt2 += RRB(r, c)
print(cnt1, cnt2)