# 백준 14621번 나만 안되는 연애 - 34%

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


def prim(v):
    heap = []
    heapq.heappush(heap, (0, v))
    dist = 0
    visited = [0] * (N+1)

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            dist += w
            visited[v] = 1
            for w, weight in graph[v]:
                if univ[v] != univ[w] and not visited[w]:
                    heapq.heappush(heap, (weight, w))
    return dist


N, M = map(int, input().split())
univ = [0] + list(input().split())
# more = '.'
# if univ.count('M') > univ.count('W'):
#     more = 'M'
# else:
#     more = 'W'
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))
ans = 987987987
# for i in range(1, len(univ)):
#     result = prim(i)
result = prim(1)
if ans > result:
    ans = result
print(ans)