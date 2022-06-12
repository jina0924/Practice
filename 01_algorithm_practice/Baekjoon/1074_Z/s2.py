# 백준 1074번 Z - 시간초과

import sys
sys.stdin = open('input.txt')


def visit(sr, sc, n):
    global cnt, ans
    if n == 1:
        for i in range(2):
            for j in range(2):
                if sr + i == r and sc + j == c:
                    ans = cnt
                    return
                cnt += 1
        return
    if r >= sr + 2 ** (n-1):
        if c >= sc + 2 ** (n-1):
            cnt += 4 ** (n-1) * 3
            visit(sr + 2 ** (n-1), sc + 2 ** (n-1), n-1)
        else:
            cnt += 4 ** (n-1) * 2
            visit(sr + 2 ** (n - 1), sc, n - 1)
    else:
        if c >= sc + 2 ** (n-1):
            cnt += 4 ** (n-1)
            visit(sr, sc + 2 ** (n-1), n-1)
        else:
            visit(sr, sc, n - 1)


for _ in range(6):
    N, r, c = map(int, input().split())
    ans, cnt = 0, 0
    visit(0, 0, N)
    print(ans)