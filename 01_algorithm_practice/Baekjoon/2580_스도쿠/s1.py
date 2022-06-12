# 백준 2580번 스도쿠

import sys
sys.stdin = open('input.txt')


def check(r, c):
    nums = [0] * 10
    for i in range(9):
        nums[board[i][c]] = 1
        nums[board[r][i]] = 1
    for s in range(r//3*3, r // 3 * 3 + 3):
        for t in range(c // 3 * 3, c // 3 * 3 + 3):
            nums[board[s][t]] = 1
    return nums


def sudoku(idx):
    global finish
    if idx >= len(blank):
        finish = True
        for row in board:
            print(*row)
        return
    rr, cc = blank[idx]
    if not board[rr][cc]:
        data = check(rr, cc)
        for i in range(1, len(data)):
            if not data[i]:
                board[rr][cc] = i
                sudoku(idx+1)
                if not finish:
                    board[rr][cc] = 0


board = [list(map(int, input().split())) for _ in range(9)]
blank = []
finish = False
for r in range(9):
    for c in range(9):
        if not board[r][c]:
            blank.append((r, c))
sudoku(0)