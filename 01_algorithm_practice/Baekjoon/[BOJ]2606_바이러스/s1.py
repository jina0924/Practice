# 백준 2606번 바이러스

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    X, Y = find_set(x), find_set(y)
    if X < Y:
        p[Y] = X
    else:
        p[X] = Y


N = int(input())
edge_cnt = int(input())
p = [i for i in range(N+1)]
for _ in range(edge_cnt):
    a, b = map(int, input().split())
    union(a, b)
ans = 0
for i in range(2, N + 1):
    p[i] = find_set(i)
    if p[i] == 1:
        ans += 1
print(ans)