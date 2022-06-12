# 백준 1992번 쿼드트리 - x

import sys
sys.stdin = open('input2.txt')


def compress(r1, c1, r2, c2):
    lt = data[r1][c1]
    rt = data[r1][c2]
    lb = data[r2][c1]
    rb = data[r2][c2]
    same = True
    print('(', end='')
    for r in range(r1, (r1 + r2) // 2 + 1):
        for c in range(c1, (c1 + c2) // 2 + 1):
            if data[r][c] != lt:
                same = False
    if not same:
        compress(r1, c1, (r1 + r2) // 2, (c1 + c2) // 2)
    else:
        print(f'{lt}', end='')
    same = True
    for r in range(r1, (r1 + r2) // 2 + 1):
        for c in range((c1 + c2) // 2 + 1, c2 + 1):
            if data[r][c] != rt:
                same = False
    if not same:
        compress(r1, (c1 + c2) // 2 + 1, (r1 + r2) // 2, c2)
    else:
        print(f'{rt}', end='')
    same = True
    for r in range((r1 + r2) // 2 + 1, r2 + 1):
        for c in range(c1, (c1 + c2) // 2 + 1):
            if data[r][c] != lb:
                same = False
    if not same:
        compress((r1 + r2) // 2 + 1, c1, r2, (c1 + c2) // 2)
    else:
        print(f'{lb}', end='')
    same = True
    for r in range((r1 + r2) // 2 + 1, r2 + 1):
        for c in range((c1 + c2) // 2 + 1, c2 + 1):
            if data[r][c] != rb:
                same = False
    if not same:
        compress((r1 + r2) // 2 + 1, (c1 + c2) // 2 + 1, r2, c2)
    else:
        print(f'{rb}', end='')
    print(')', end='')


N = int(input())
data = [list(map(int, input())) for _ in range(N)]
compress(0, 0, N-1, N-1)