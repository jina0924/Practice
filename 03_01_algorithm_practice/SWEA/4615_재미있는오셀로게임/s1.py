# SWEA 4615. 재미있는 오셀로 게임

import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 한 변의 길이, M: 플레이어가 돌을 놓는 횟수
    board = [[0] * N for _ in range(N)]
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 1
    board[N//2 - 1][N//2 - 1] = board[N//2][N//2] = 2
    for _ in range(M):
        r, c, color = map(int, input().split())
        board[r-1][c-1] = color
        queue = deque([(r-1, c-1)])
        while True:
            rr, cc = queue.pop()
            for d in range(8):
                nr, nc = rr + delta[d][0], cc + delta[d][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] != color:
                        queue.append((nr, nc))
                    else:
                        board[rr][cc] = color
        # for i in range(N):
        #     if board[i][c-1] == color:
        #         if i > r-1:
        #             for k in range(r-1, i):
        #                 board[k][c-1] = color
        #         else:
        #             for k in range(i+1, r):
        #                 board[k][c-1] = color
        # for j in range(N):
        #     if board[r-1][j] == color:
        #         if j > c-1:
        #             for k in range(c-1, j):
        #                 board[r-1][k] = color
        #         else:
        #             for k in range(j+1, c):
        #                 board[r-1][k] = color

    print('#{} {}'.format(tc, board))

