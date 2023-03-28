# 백준 18116번 로봇 조립 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    px, py = find_set(x), find_set(y)
    if px < py:
        p[py] = px
    else:
        p[px] = py


N = int(input())
p = [i for i in range(1000001)]
for _ in range(N):
    direc = input().split()
    if direc[0] == 'I':
        union(int(direc[1]), int(direc[2]))
    else:
        tmp = find_set(int(direc[1]))
        print(p.count(tmp))