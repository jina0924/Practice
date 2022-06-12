# SWEA 1865. 동철이의 일 분배 - 시간초과

import sys
sys.stdin = open('input.txt')


def work(r):
    global p, ans
    if r > N-1:
        if p > ans:
            ans = p
        return

    for c in range(N):
        if not done[c] and data[r][c]:
            p *= data[r][c] / 100
            done[c] = 1
            work(r+1)
            done[c] = 0
            p /= data[r][c] / 100


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    done = [0] * N
    p, ans = 1, 0
    work(0)
    print('#{} {:.6f}'.format(tc, ans * 100))