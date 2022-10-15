# 백준 2667번 단지 번호 붙이기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(r, c, cnt):
    queue = [(r, c)]
    visited[r][c] = 1
    total = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and data[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                data[nr][nc] = cnt
                total += 1
                queue.append((nr, nc))
    return total


cnt = 0
ans = []
for r in range(N):
    for c in range(N):
        if data[r][c] and not visited[r][c]:
            cnt += 1
            ans.append(bfs(r, c, cnt))
print(cnt)
for res in sorted(ans):
    print(res)