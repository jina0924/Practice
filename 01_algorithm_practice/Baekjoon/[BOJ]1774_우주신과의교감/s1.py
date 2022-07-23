# 백준 1774번 우주신과의 교감

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


# def dijkstra():
#     heap = []
#     heapq.heappush(heap, (0, 0))
#
#     while heap:
#         w, v = heapq.heappop(heap)
#         if not visited[v]:
#             visited[v] = 1
#             dist[v] = w
#             for i in range(N+1):
#                 if not visited[i]:
#                     heapq.heappush(heap, (dist[v] + G[v][i], i))
#     return dist[N]

N, M =map(int, input().split())
data = []
linked = []
w = h = 0
for _ in range(N):
    r, c = map(int, input().split())
    w, h = max(w, r), max(h, c)
    data.append((r, c))
visited = [0] * (N+1)
# G = [[987987987] for _ in range(N+1) for _ in range(N+1)]
# dist = [987987987] * (N+1)
# for _ in range(M):
#     a, b = map(int, input().split())
#     dist[a] = 0
