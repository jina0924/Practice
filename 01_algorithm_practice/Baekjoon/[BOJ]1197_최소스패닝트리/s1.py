# 백준 1197번 최소 스패닝 트리

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
from collections import defaultdict


def prim(v):
    heap = [(0, v)]
    cnt = 0
    visited[v] += 1

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            cnt += w
            visited[v] += 1
        for nv, nw in graph[v]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv))
    return cnt


V, E = map(int, input().split())
graph = defaultdict(list)                   # 메모리 초과 해결하기 위해 이차원 배열대신 인접리스트 사용
visited = [0] * (V + 1)
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
print(prim(1))