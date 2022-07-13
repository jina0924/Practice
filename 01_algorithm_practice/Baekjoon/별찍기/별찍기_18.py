# 백준 10993번 별 찍기-18

import sys
input = sys.stdin.readline


def star(n, start):
    if n == 0:
        return
    m = (size[n-1][1] - 1) // 2
    r = start
    if n % 2:
        while r < size[n-1][0] - 1:
            board[r][m-r] = board[r][m+r] = '*'
            r += 1
        for i in range(size[n-1][1]):
            board[r][i] = '*'
        star(n-1, r-1)
    if n % 2 == 0:
        while r:
            board[r][m-r] = board[r][m+r] = '*'
            r -= 1
        for i in range(size[n-1][1]):
            board[r][i] = '*'
        star(n-1, r+1)


N = int(input())

size = [(1, 1)]
h = w = cnt = 1
while cnt < N:
    h = h * 2 + 1
    w = 2 * h - 1
    size.append((h, w))
    cnt += 1

board = [[''] * w for _ in range(h)]
if N % 2:
    star(N, 0)
elif N % 2 == 0:
    star(N, h-1)
print(board)
