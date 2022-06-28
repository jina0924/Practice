# 백준 1261번 알고스팟

import sys
sys.stdin = open('input3.txt')
import heapq

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def smash():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    visited[0][0] = 1

    while heap:
        cnt, r, c = heapq.heappop(heap)
        if r == n-1 and c == m-1:
            return cnt
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = 1
                if maze[nr][nc]:
                    heapq.heappush(heap, (cnt+1, nr, nc))
                elif maze[nr][nc] == 0:
                    heapq.heappush(heap, (cnt, nr, nc))


m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(smash())