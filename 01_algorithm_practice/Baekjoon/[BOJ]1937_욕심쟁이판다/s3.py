 # 백준 1937번 욕심쟁이 판다

import sys
sys.stdin = open('input.txt')

n = int(input())
forest = []                                 # 대나무숲 정보
bamboo = []                                 # 대나무 양과 위치 값 담을 리스트
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        bamboo.append((data[c], r, c))
    forest.append(data)
bamboo.sort(reverse=True)                   # 대나무 양 많은 순으로 정렬
result = [[1] * n for _ in range(n)]        # 이동 경로 담을 이차원 리스트
i = 0                                       # 살펴볼 대나무 인덱스 값
ans = 1                                     # 최대 경로
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
while i < len(bamboo):
    w, r, c = bamboo[i]
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and forest[nr][nc] < w:
            # 새로 살펴보는 쪽에 저장된 경로 값이 지금 위치에서 한 칸 이동한 값 보다 작을때만 갱신해줌
            if result[nr][nc] < result[r][c] + 1:
                result[nr][nc] = result[r][c] + 1
            if ans < result[nr][nc]:
                ans = result[nr][nc]
    i += 1
print(ans)