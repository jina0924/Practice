# 백준 1697번 숨바꼭질

import sys
sys.stdin = open('input.txt')
from collections import deque


def find(n):
    queue = deque([(n, 0)])
    visited = [0] * 100001

    while queue:
        p, s = queue.popleft()
        visited[p] = 1
        if p == K:
            return s
        for np in (p+1, p-1, 2*p):
            if 0 <= np <= 100000 and not visited[np]:
                queue.append((np, s+1))


N, K = map(int, input().split())
if K <= N:
    print(N - K)
else:
    print(find(N))