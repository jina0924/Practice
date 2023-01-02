# 백준 10216번 Count Circle Groups

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    N = int(input())
    # data = [[0] * N for _ in range(N)]
    for n in range(1, N + 1):
        x, y, R = map(int, input().split())
        data[N - y - 1][x] = n
    print(data)
