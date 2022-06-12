# 백준 1149번 RGB거리

import sys
sys.stdin = open('input.txt')


def coloring():
    i = 1
    while i < N:
        data[i][0] += min(data[i-1][1], data[i-1][2])
        data[i][1] += min(data[i-1][0], data[i-1][2])
        data[i][2] += min(data[i-1][0], data[i-1][1])
        i += 1
    print(min(data[N-1]))

for tc in range(5):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    coloring()