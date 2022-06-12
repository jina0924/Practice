# SWEA 1795. 인수의 생일 파티

import sys
sys.stdin = open('input.txt')
import heapq


def dijkstra_out(dist, visited):
    heap = []
    heapq.heappush(heap, (0, X))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for i in range(1, N+1):
                if G[v][i] and not visited[i]:
                    heapq.heappush(heap, (w + G[v][i], i))

def dijkstra_in(dist, visited):
    heap = []
    heapq.heappush(heap, (0, X))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for i in range(1, N+1):
                if G[i][v] and not visited[i]:
                    heapq.heappush(heap, (w + G[i][v], i))


T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())         # N: 정점 개수, M: 간선 개수, X: 도착지
    G = [[987987987] * (N+1) for _ in range(N+1)]
    dist_out = [987987987] * (N+1)
    dist_out[0] = dist_out[X] = 0
    visited_out = [0] * (N+1)
    dist_in = [987987987] * (N+1)
    dist_in[0] = dist_in[X] = 0
    visited_in = [0] * (N+1)
    for _ in range(M):
        x, y, c = map(int, input().split())     # x번 집에서 y번 집으로 가는데 c시간 걸리는 단 방향 도로
        G[x][y] = c
    dijkstra_out(dist_out, visited_out)
    dijkstra_in(dist_in, visited_in)
    for i in range(N+1):
        dist_out[i] += dist_in[i]
    ans = max(dist_out)
    print(f'#{tc} {ans}')