# 백준 16918번 봄버맨

import sys
sys.stdin = open('input4.txt')
input = sys.stdin.readline


def bomberman(s):
    if s % 2 == 0:                                  # 짝수 초일때 -> 모든 칸에 폭탄 설치됨
        for r in range(R):
            print('O' * C)
    else:
        bomb1 = [['O'] * C for _ in range(R)]       # 첫 번째로 설치한 폭탄이 터진 data를 저장할 2차원 배열
        for r in range(R):
            for c in range(C):
                if data[r][c] == 'O':               # 이번에 터질 폭탄이라면
                    bomb1[r][c] = '.'               # 현재 위치 터짐
                    for d in range(4):              # 현재 위치 기준으로 사방도 터짐
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < R and 0 <= nc < C:
                            bomb1[nr][nc] = '.'

        if s % 4 == 3:                              # 3, 7, 11...번째 = 첫 번째로 설치한 폭탄 터지는 상황
            for r in range(R):
                print(*bomb1[r], sep='')
            return

        bomb2 = [['O'] * C for _ in range(R)]       # 두 번째로 설치한 폭탄이 터진 data
        for r in range(R):
            for c in range(C):
                if bomb1[r][c] == 'O':              # 첫 번째로 설치한 폭탄이 터진 이후에 살아남은 폭탄 = 이번에 터짐
                    bomb2[r][c] = '.'
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < R and 0 <= nc < C:
                            bomb2[nr][nc] = '.'

        if s % 4 == 1:                            # 5, 9, 13...번째 = 두 번째로 설치한 폭탄이 터지는 상황
            for r in range(R):
                print(*bomb2[r], sep='')


R, C, N = map(int, input().split())                 # RxC 격자판, N초
data = [list(input().rstrip()) for _ in range(R)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
if N > 1:
    bomberman(N)
else:
    for r in range(R):
        print(*data[r], sep='')