# 백준 11559번 Puyo Puyo

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def puyoPop():
    visited = [[0] * 6 for _ in range(12)]
    combo = 0

    for puyo in spot:
        queue = [puyo]
        color = field[puyo[0]][puyo[1]]
        isPop = False
        temp = []
        visited[puyo[0]][puyo[1]] = 1
        cnt = 0

        while queue:
            cr, cc = queue.pop(0)
            temp.append((cr, cc))
            cnt += 1
            if cnt >= 4:
                isPop = True
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < 12 and 0 <= nc < 6 and field[nr][nc] == color and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1

        if isPop:
            combo = 1
            for t in temp:
                field[t[0]][t[1]] = '.'
    return combo


def puyoDown():
    new_spot = []

    for c in range(6):
        queue = []
        for r in range(11, top-1, -1):
            if field[r][c] != '.':
                queue.append(field[r][c])
        for r in range(11, top-1, -1):
            if queue:
                field[r][c] = queue.pop(0)
                new_spot.append((r, c))
            else:
                field[r][c] = '.'
    return new_spot


field = []
top = 12
spot = []
for r in range(12):
    data = list(input().rstrip())
    if data.count('.') != 6:
        for c in range(6):
            if data[c] != '.':
                spot.append((r, c))
        if top > r:
            top = r
    field.append(data)

result = 0
while True:
    if puyoPop():
        spot = puyoDown()
        result += 1
    else:
        print(result)
        break
