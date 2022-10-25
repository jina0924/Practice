# 백준 16918번 봄버맨

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline


def bomberman(s):
    if s % 2:
        for r in range(R):
            for c in range(C):
                if data[r][c] == 'o':
                    data[r][c] = 1
                else:
                    data[r][c] = 0
    else:
        for r in range(R):
            for c in range(C):
                if data[r][c] > 0:
                    data[r][c] = '.'
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < R and 0 <= nc < C:
                            data[nr][nc] = '.'
                else:
                    data[r][c] += 1


R, C, N = map(int, input().split())
data = [list(input().rstrip()) for _ in range(R)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
print(data)
for s in range(N):
    bomberman(s)