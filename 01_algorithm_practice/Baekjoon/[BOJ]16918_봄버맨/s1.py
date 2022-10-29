# 백준 16918번 봄버맨 - x

import sys
sys.stdin = open('input4.txt')
input = sys.stdin.readline


def bomberman(s):
    if s % 2 == 0 or s % 4 == 3:
        for r in range(R):
            for c in range(C):
                data[r][c] = 'O'
        if s % 4 == 3:
            for b in bomb:
                r, c = b
                data[r][c] = '.'
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C:
                        data[nr][nc] = '.'


R, C, N = map(int, input().split())
data = []
bomb = []
for r in range(R):
    data.append(list(input().rstrip()))
    for c in range(C):
        if data[r][c] == 'O':
            bomb.append((r, c))
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
bomberman(N)
for r in range(R):
    print(*data[r], sep='')