# SWEA 1249. 보급로

import sys
sys.stdin = open('input.txt')
import heapq

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]              # 상, 하, 좌, 우
def dijkstra(r, c):
    heap = []
    heapq.heappush(heap, (0, r, c))                     # 처음 넘겨받은 인자 넣어주기

    while r != N-1 or c != N-1:                         # 도착지에 다다를때까지 반복
        w, r, c = heapq.heappop(heap)                   # w: 파여진 도로 깊이(복구 시간) / r , c: 좌표 값
        if visited[r][c]:                               # 이미 들른 곳이라면 더 적은 복구 시간으로 들렀을 것
            continue
        data[r][c] += w                                 # 넘겨받은 시간 누적해줌
        visited[r][c] = 1                               # 방문 표시
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    heapq.heappush(heap, (data[r][c], nr, nc))      # 가중치 적은 순으로 나열 됨

    return data[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())                                    # N: 지도의 가로 세로 크기
    data = [list(map(int, input())) for _ in range(N)]      # 지도 정보
    visited = [[0] * N for _ in range(N)]               # 지도의 각 부분 방문체크 배열
    ans = dijkstra(0, 0)
    print(f'#{tc} {ans}')