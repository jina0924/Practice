# SWEA 5251. 최소 이동 거리

import sys
sys.stdin = open('input.txt')
from collections import deque


def BFS(v, w):
    queue = deque([(v, w)])
    minV = 10000000

    while queue:
        v, w = queue.popleft()
        if minV <= w:                               # 가지치기: 지금까지 살펴본 거리가 minV 이상이라면
            continue                                # 더 이상 안봐도 됨
        for i in range(N+1):
            if G[v][i]:                             # 현재 위치와 연결된 지점이고
                if i == N:                          # 그 지점이 도착지(N)이라면
                    if minV > w + G[v][i]:          # 지금까지의 거리값과 minV를 비교해서 작은 값으로 갱신
                        minV = w + G[v][i]
                else:                               # 연결된 지점이 도착지가 아니라면
                    queue.append((i, w + G[v][i]))      # 큐에 넣어주고 다음에 방문함

    return minV


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())        # N: 마지막 연결지점 번호, E: 도로의 개수
    G = [[0] * (N+1) for _ in range(N+1)]   # 연결 지점을 표시할 그래프
    for _ in range(E):
        s, e, w = map(int, input().split())     # s: 구간 시작점, e: 구간 끝 지점, w: 구간 거리
        G[s][e] = w                         # 일방통행 도로이므로 s -> e에만 거리 표시해줌
    print(f'#{tc} {BFS(0, 0)}')