# 백준 1260번 DFS와 BFS

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline
from collections import deque


def dfs(v):
    # stack = deque([v])
    #
    # while stack:
    #     cv = stack.pop()
    #     if not visited[cv]:
    #         visited[cv] = 1
    #         print(cv, end=' ')
        # for nv in range(N, 0, -1):
        #     if graph[cv][nv] and not visited[nv]:
        # for nv in graph[cv]:
        #     if not visited[nv]:
        #         dfs(nv)
    visited[v] = 1
    print(v, end=' ')
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


def bfs(v):
    queue = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1

    while queue:
        cv = queue.popleft()
        print(cv, end=' ')
        # for nv in range(1, N+1):
        #     if graph[cv][nv] and not visited[nv]:
        for nv in graph[cv]:
            if not visited[nv]:
                queue.append(nv)
                visited[nv] = 1


N, M, V = map(int, input().split())
# graph = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    # graph[s][e] = graph[e][s] = 1
    graph[s].append(e)
    graph[e].append(s)
for g in graph:
    g.sort()
visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
