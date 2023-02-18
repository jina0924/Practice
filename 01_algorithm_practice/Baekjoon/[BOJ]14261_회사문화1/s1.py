# 백준 14267번 회사 문화1 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque

n, m = map(int, input().split())
data = list(map(int, input().split()))
tree = defaultdict(list)
for i in range(1, n):
    tree[data[i]].append(i+1)
ans = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    queue = deque([(i)])
    ans[i] += w
    while queue:
        now = queue.popleft()
        for c in tree[now]:
            ans[c] += w
            queue.append(c)
print(*ans[1:])