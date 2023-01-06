# 백준 2566번 최대값

import sys
sys.stdin = open('input.txt')

matrix = [list(map(int, input().split())) for _ in range(9)]

ans, rr, cc = 0, 0, 0
for r in range(9):
    for c in range(9):
        if matrix[r][c] > ans:
            ans = matrix[r][c]
            rr, cc = r, c
print(ans)
print(rr + 1, cc + 1)