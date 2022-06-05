# 백준 1992번 쿼드트리

import sys
sys.stdin = open('input2.txt')


def compress(r1, c1, r2, c2):
    rep = data[r1][c1]
    same = True
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if data[r][c] != rep:
                same = False
    if same:
        print(rep, end='')
    else:
        print('(', end='')
        compress(r1, c1, (r1 + r2) // 2, (c1 + c2) // 2)
        compress(r1, (c1 + c2) // 2 + 1, (r1 + r2) // 2, c2)
        compress((r1 + r2) // 2 + 1, c1, r2, (c1 + c2) // 2)
        compress((r1 + r2) // 2 + 1, (c1 + c2) // 2 + 1, r2, c2)
        print(')', end='')


N = int(input())
data = [list(map(int, input())) for _ in range(N)]
compress(0, 0, N-1, N-1)