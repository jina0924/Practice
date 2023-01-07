# 백준 2738번 행렬 덧셈

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(M):
        matrix[r][c] += row[c]
    print(*matrix[r])
# for row in matrix:
#     print(*row)