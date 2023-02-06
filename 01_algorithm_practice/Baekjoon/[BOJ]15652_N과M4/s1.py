# 백준 15652번 N과 M(4)

import sys
sys.stdin = open('input3.txt')


def sequence(start, cnt):
    if cnt <= 0:
        print(*ans)
        return
    for n in range(start, N+1):
        ans[M - cnt] = n
        sequence(n, cnt-1)
        ans[M - cnt] = 0


N, M = map(int, input().split())
ans = [0] * M
sequence(1, M)