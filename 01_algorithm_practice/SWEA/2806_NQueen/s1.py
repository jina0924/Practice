# SWEA 2806. NQueen

import sys
sys.stdin = open('input.txt')


def nqueen(r):
    global cnt
    if r >= N:                  # 마지막 행까지 퀸을 놓았다면
        cnt += 1                # 성공한 경우의 수 1 올려줌
        return

    '''
    퀸이 놓여졌을 때 공격할 수 있는 위치 : 같은 행, 열, 대각선
    -> 행을 하나씩 늘려가면서 퀸을 놓으므로 행에 대한 visited는 필요x
    -> for문을 돌면서 해당 위치의 열, 대각선에 지난 번에 위치한 퀸이 있는지 없는지 조사하고
    없다면 해당 위치에 퀸을 놓고 다음 행 살펴봄
    => 살펴보고 돌아왔을 때 해당 위치의 방문 표시 초기화해서 같은 행의 다른 위치 살펴봄
    '''
    for i in range(N):
        if not c_visited[i] and not d1_visited[r+i] and not d2_visited[r-i+N-1]:
            c_visited[i] = 1
            d1_visited[r+i] = 1
            d2_visited[r-i+N-1] = 1
            nqueen(r+1)
            c_visited[i] = 0
            d1_visited[r + i] = 0
            d2_visited[r - i + N - 1] = 0
    else:                       # 가지치기 : 해당 행에서 갈 수 있는 부분이 없다면 함수 탈출
        return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0] * 8 for _ in range(8)]
    c_visited = [0] * N                 # 열 방문 체크
    d1_visited = [0] * (N + N-1)        # y = x 모양 대각선 방문 체크
    d2_visited = [0] * (N + N-1)        # y = -x 모양 대각선 방문 체크
    cnt = 0                             # N개의 queen을 놓을 수 있는 경우의 수
    nqueen(0)                           # 첫 번째 행 부터 퀸 놓음
    print(f'#{tc} {cnt}')