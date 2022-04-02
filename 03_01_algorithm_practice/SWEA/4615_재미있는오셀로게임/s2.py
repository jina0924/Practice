# SWEA 4615. 재미있는 오셀로 게임

import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 한 변의 길이, M: 플레이어가 돌을 놓는 횟수
    board = [[0] * N for _ in range(N)]
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 1
    board[N//2 - 1][N//2 - 1] = board[N//2][N//2] = 2
    position = {
        1: [[N//2 - 1, N//2], [N//2, N//2 - 1]],
        2: [[N//2 - 1, N//2 - 1], [N//2, N//2]]
    }
    for _ in range(M):
        r, c, color = map(int, input().split())
        board[r-1][c-1] = color
        for pos in position.get(color):
            if pos[0] == r-1:
                if pos[1] < c-1:
                    for k in range(pos[1], c):
                        position[color].append([r-1, k])


    print('#{} {}'.format(tc, board))

