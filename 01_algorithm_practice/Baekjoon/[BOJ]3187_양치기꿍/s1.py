# 백준 3187번 양치기 꿍

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(r, c):
    queue = [(r, c)]
    wolf, sheep = 0, 0
    if data[r][c] == 'v':
        wolf += 1
    elif data[r][c] == 'k':
        sheep += 1
    data[r][c] = '#'

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and data[nr][nc] != '#':
                queue.append((nr, nc))
                if data[nr][nc] == 'v':
                    wolf += 1
                elif data[nr][nc] == 'k':
                    sheep += 1
                data[nr][nc] = '#'
    return wolf, sheep


R, C = map(int, input().split())
data = [list(input().rstrip()) for _ in range(R)]
total_v, total_k = 0, 0
for r in range(R):
    for c in range(C):
        if data[r][c] == 'k' or data[r][c] == 'v':
            v, k = bfs(r, c)
            if k > v:
                total_k += k
            else:
                total_v += v
print(total_k, total_v)