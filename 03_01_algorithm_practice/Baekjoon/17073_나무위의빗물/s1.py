# 백준 17073번 나무 위의 빗물 - 메모리 초과

import sys
sys.stdin = open('input.txt')
from collections import deque


def find_leaf(v):
    global cnt
    stack = deque([v])

    while stack:
        v = stack.popleft()
        is_leaf = True
        for node in range(1, N+1):
            if node != v and G[v][node] and not parent[node]:
                stack.append(node)
                parent[v] = 1
                is_leaf = False
        if is_leaf:
            cnt += 1


N, W = map(int, input().split())        # N: 노드의 수, W: 1번 노드에 고인 물의 양
G = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    G[U][V] = G[V][U] = 1
parent = [1] + [0] * (N)
cnt = 0
find_leaf(1)
print(W / cnt)
