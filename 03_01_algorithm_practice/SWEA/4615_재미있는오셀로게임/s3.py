# SWEA 4615. 재미있는 오셀로 게임 - 완성

import sys
sys.stdin = open('input.txt')

'''
델타 방향을 하나로 고정해서 현재 둔 돌과 같은 색의 돌을 찾을 때까지 반복함
현재 돌과 같은 색의 돌을 찾았다면 flag를 True로 바꿔주고
호출했던 함수(다른 색 돌)로 돌아오면서 돌을 변경해줌
'''

# 12시부터 시계방향으로
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def otehllo(r, c, d, color):
    global flag
    nr, nc = r + delta[d][0], c + delta[d][1]
    if 0 <= nr < N and 0 <= nc < N:
        if board[nr][nc] and board[nr][nc] != color:
            otehllo(nr, nc, d, color)
            if flag:
                board[nr][nc] = color
        elif board[nr][nc] == color:
            flag = True
            return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())                    # N: 한 변의 길이, M: 플레이어가 돌을 놓는 횟수
    board = [[0] * N for _ in range(N)]
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 1   # 가운데 돌은 항상 위치 정해져 있음(WB/BW)
    board[N//2 - 1][N//2 - 1] = board[N//2][N//2] = 2
    for _ in range(M):
        r, c, color = map(int, input().split())
        for d in range(8):                              # 가로, 세로, 대각선 모두 살펴봐줌
            flag = False                                # 현재 위치에서 떨어진 같은 색 돌 찾음을 나타낼 플래그 변수
            otehllo(r-1, c-1, d, color)
        board[r-1][c-1] = color                         # 함수 다 돌고 현재 위치에 돌 놔줌

    black, white = 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))

