# SWEA 5250. 최소 비용

import sys
sys.stdin = open('input.txt')
import heapq

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def sol():
    heap = []
    heapq.heappush(heap, (0, 0, 0))                     # 가중치, 좌표 순서대로 힙에 넣어줌(초기 좌표 (0, ))

    while heap:
        w, r, c = heapq.heappop(heap)
        if not visited[r][c]:                           # 방문하지 않은 곳이라면 중복 방문 피하기 위해
            visited[r][c] = 1                           # 방문 표시 해주고
            fuel[r][c] = w                              # 해당 좌표까지 필요한 연료(가중치) 입력
            if r == N-1 and c == N-1:
                return fuel[N-1][N-1]
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    f = 1                               # 1칸 이동하는데 필요한 연로 1로 초기화
                    if data[nr][nc] > data[r][c]:       # 만약 지금 위치보다 높다면
                        f += data[nr][nc] - data[r][c]      # 높은 만큼 연료 더해줌
                    heapq.heappush(heap, (w+f, nr, nc))     # 해당 위치까지 가는데 필요한 연료가중치와 좌표 힙에 넣어줌


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                                    # N: 가로, 세로 칸 수
    data = [list(map(int, input().split())) for _ in range(N)]      # 각 지역 높이 정보
    fuel = [[987654321] * N for _ in range(N)]          # 연료 소비량 초기화
    visited = [[0] * N for _ in range(N)]               # 지도의 각 부분 방문체크 배열
    print(f'#{tc} {sol()}')