# SWEA 5188. 최소합

import sys
sys.stdin = open('input.txt')


def dfs(r, c, total):
    global ans
    if r == N-1 and c == N-1:                   # 마지막 위치에 도달했다면
        if total < ans:                         # 이동하면서 구한 합계가 최소합인지 살펴보기
            ans = total

    if r + 1 < N:                               # 만약 한 칸 내려간 위치가 숫자판 안에 있다면
        dfs(r+1, c, total + data[r+1][c])       # 해당 값 더하면서 내려감
    if c + 1 < N:                               # 만약 한 칸 오른쪽으로 이동한 위치가 숫자판 안에 있다면
        dfs(r, c+1, total + data[r][c+1])       # 해당 값 더하면서 이동함

T = int(input())

for tc in range(1, T+1):
    N = int(input())                            # N: 가로, 세로의 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 250                                   # N의 최대값 = 13, 각 요소의 최대값 = 10
    dfs(0, 0, data[0][0])
    print(f'#{tc} {ans}')