# SWEA 1795. 인수의 생일 파티

import sys
sys.stdin = open('input.txt')
import heapq


def dijkstra(G):
    heap = []
    heapq.heappush(heap, (0, X))
    dist = [987987987] * (N+1)
    dist[0] = dist[X] = 0
    visited = [0] * (N+1)

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for node, weight in G[v]:
                if not visited[node]:
                    heapq.heappush(heap, (w + weight, node))
    return dist


T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())         # N: 정점 개수, M: 간선 개수, X: 도착지
    G_out = [[]for _ in range(N+1)]             # y -> x로 가는 그래프
    G_in = [[] for _ in range(N+1)]             # x -> y로 가는 그래프
    for _ in range(M):
        x, y, c = map(int, input().split())     # x번 집에서 y번 집으로 가는데 c시간 걸리는 단 방향 도로
        G_in[x].append((y, c))
        G_out[y].append((x, c))
    dist_out = dijkstra(G_out)                  # X에서 원래 집으로 가는 최단 시간
    dist_in = dijkstra(G_in)                    # 집에서 X로 가는 최단 시간
    for i in range(N+1):                        # 갈 때와 올 때의 걸리는 시간 더해줌
        dist_out[i] += dist_in[i]
    ans = max(dist_out)                         # 가장 오래거리는 시간 출력
    print(f'#{tc} {ans}')