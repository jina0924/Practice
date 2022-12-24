# 백준 14502번 연구소

import sys
from copy import deepcopy
sys.stdin = open('input3.txt')


def wall(cnt, cr, cc):
    global ans
    if cnt >= 3:                                # 벽을 세 개 이상 세웠다면
        result = bfs()                          # 안전 영역의 크기 세러 감
        if result > ans:                        # 이번에 구한 안전 영역의 크기가 최대값이라면 갱신
            ans = result
    else:
        for r in range(N):
            for c in range(M):
                if data[r][c] == 0 and (r > cr or c >= cc):     # 빈 칸이고 전에 살펴본 위치보다 전이 아니라면
                    data[r][c] = 1                              # 벽 세우고
                    wall(cnt + 1, r, c)                         # 현재 벽 개수에 + 1하기
                    data[r][c] = 0                              # 벽 세운 것 초기화


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    lab = deepcopy(data)                        # 현재 벽 세운 연구소 상태
    queue = deepcopy(virus)                     # 바이러스 위치

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


N, M = map(int, input().split())                # N, M: 지도의 세로, 가로 크기
data = []                                       # 연구소 지도
virus = []                                      # 바이러스 위치 값
ans = 0                                         # 안전 영역의 최대 크기 담을 배열
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(M):
        if row[c] == 2:                         # 바이러스 위치 저장
            virus.append((r, c))
    data.append(row)
wall(0, 0, 0)
print(ans)