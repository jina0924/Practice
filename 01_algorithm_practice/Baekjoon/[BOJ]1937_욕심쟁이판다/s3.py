 # 백준 1937번 욕심쟁이 판다

import sys
sys.stdin = open('input.txt')

n = int(input())
forest = []
bamboo = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        bamboo.append((data[c], r, c))
    forest.append(data)
bamboo.sort(reverse=True)
result = [[1] * n for _ in range(n)]
i = 0
ans = 1
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
while i < len(bamboo):
    w, r, c = bamboo[i]
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and forest[nr][nc] < w:
            if result[nr][nc] < result[r][c] + 1:
                result[nr][nc] = result[r][c] + 1
            if ans < result[nr][nc]:
                ans = result[nr][nc]
    i += 1
print(ans)