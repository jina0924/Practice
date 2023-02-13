# 백준 9372번 상근이의 여행

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def union(x, y):
    p[find_set(y)] = find_set(x)


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for x in range(1, N + 1):
        p[x] = find_set(x)
    print(p)
