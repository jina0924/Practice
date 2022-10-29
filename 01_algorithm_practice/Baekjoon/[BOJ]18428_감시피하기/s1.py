# 백준 18428번 감시피하기

import sys
sys.stdin = open('input2.txt')


def check():
    global ans

    for t in teachers:
        cr, cc = t
        d = 0
        while d < 4:
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] == 'S':
                    return
                elif data[nr][nc] == 'O':
                    d += 1
                    cr, cc = t
                else:
                    cr, cc = nr, nc
            else:
                d += 1
                cr, cc = t
    ans = 'YES'


def hide(cnt):
    if cnt >= 3:
        check()
        return
    for r in range(N):
        for c in range(N):
            if data[r][c] == 'X':
                data[r][c] = 'O'
                hide(cnt + 1)
                data[r][c] = 'X'


N = int(input())
data = []
teachers = []
for r in range(N):
    row = list(input().split())
    data.append(row)
    for c in range(N):
        if row[c] == 'T':
            teachers.append((r, c))
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 'NO'
hide(0)
print(ans)