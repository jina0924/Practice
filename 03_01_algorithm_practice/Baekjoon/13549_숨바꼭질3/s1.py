# 백준 13549번 숨바꼭질3 - 7프로 시간초과

import sys
sys.stdin = open('input2.txt')
import heapq


def dijkstra():
    heap = []
    x = N
    while x <= 100000:
        heapq.heappush(heap, (0, x))
        x *= 2

    while heap:
        w, v = heapq.heappop(heap)
        # if not visited[v]:
        #     visited[v] = 1
        #     dist[v] = w
        if v == K:
            return dist[K]
        left, right = v - 1, v + 1
        if 0 <= left <= 100000 and not visited[left]:
            while left <= 100000:
                if not visited[left]:
                    heapq.heappush(heap, (w + 1, left))
                    visited[left] = 1
                    dist[left] = w + 1
                left *= 2
        if 0 <= right <= 100000 and not visited[right]:
            while right <= 100000:
                if not visited[right]:
                    heapq.heappush(heap, (w + 1, right))
                    visited[right] = 1
                    dist[right] = w + 1
                right *= 2


N, K = map(int, input().split())        # N: 수빈이의 위치, K: 동생의 위치
dist = [987987987] * 100001
dist[N] = 0
visited = [0] * 100001
if K < N:
    print(N-K)
else:
    print(dijkstra())
