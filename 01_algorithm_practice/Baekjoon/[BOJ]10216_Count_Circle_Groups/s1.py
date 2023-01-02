# 백준 10216번 Count Circle Groups

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    N = int(input())
    data = [[0] * N for _ in range(N)]
    x, y, R = map(int, input().split())
    data[x][y] = 1
