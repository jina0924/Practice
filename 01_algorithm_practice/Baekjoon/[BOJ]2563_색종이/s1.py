# 백준 2563번 색종이

import sys
sys.stdin = open('input.txt')

board = [[0] * 100 for _ in range(100)]
cnt = int(input())
for _ in range(cnt):
    c, r = map(int, input().split())
    r, c = 89 - r, c - 1
    for rr in range(r, r + 10):
        for cc in range(c, c + 10):
            board[rr][cc] = 1
ans = 0
for row in board:
    ans += row.count(1)
print(ans)