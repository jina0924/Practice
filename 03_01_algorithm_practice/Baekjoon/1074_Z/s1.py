# 백준 1074번 Z - 시간초과

import sys
sys.stdin = open('input.txt')


def visit(sr, sc, n):
    global cnt, stop, ans
    if n == 1:
        for i in range(2):
            for j in range(2):
                if sr + i == r and sc + j == c:
                    stop = True
                    ans = cnt
                    return
                cnt += 1
        return
    visit(sr, sc, n-1)
    if not stop:
        visit(sr, sc + 2 ** (n-1), n-1)
        if not stop:
            visit(sr + 2 ** (n-1), sc, n-1)
            if not stop:
                visit(sr + 2 ** (n-1), sc + 2 ** (n-1), n-1)


for _ in range(6):
    N, r, c = map(int, input().split())
    stop, ans, cnt = False, 0, 0
    visit(0, 0, N)
    print(ans)