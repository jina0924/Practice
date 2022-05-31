# 백준 1697번 숨바꼭질

import sys
sys.stdin = open('input.txt')
import heapq


def find(n):
    heap = []
    heapq.heappush(heap, (0, n))
    visited = [0] * 100001

    while heap:
        s, p = heapq.heappop(heap)
        visited[p] = 1
        if p == K:
            return s
        for np in (p+1, p-1, 2*p):
            if 0 <= np <= 100000 and not visited[np]:
                heapq.heappush(heap, (s+1, np))


N, K = map(int, input().split())
if K <= N:
    print(N - K)
else:
    print(find(N))