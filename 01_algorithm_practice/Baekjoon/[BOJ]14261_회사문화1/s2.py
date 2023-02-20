# 백준 14267번 회사 문화1 - recursion error

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline
from collections import defaultdict


def sol(v):
    if v <= 1:
        return 0
    else:
        result = praise[v] + sol(data[v - 1])
        ans[v] = result
        return result


n, m = map(int, input().split())
data = list(map(int, input().split()))
tree = defaultdict(list)
for i in range(1, n):
    tree[data[i]].append(i+1)
ans = [0] * (n+1)
praise = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    praise[i] += w
for j in range(n, 1, -1):
    if not ans[j]:
        ans[j] = sol(j)
print(*ans[1:])