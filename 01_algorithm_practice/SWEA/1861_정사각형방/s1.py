# SWEA 1861. 정사각형방

import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(r, c):
    queue = deque([(r, c)])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]              # 상, 하, 좌, 우
    visited[r][c] = 1
    sol = [room[r][c]]                                      # 함수로 넘겨받은 위치에서부터 갈 수 있는 곳 담을 리스트

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]: # 범위 안에 있고, 방문하지 않은 곳 중에서
                # 방 번호의 차이가 1인 경우
                # 번호가 1 큰 수로 찾지 않는 이유: 1과 2가 붙어있을 때 2 먼저 살펴보면 1을 방문할 수 없기 때문
                if abs(room[nr][nc] - room[r][c]) == 1:
                    queue.append((nr, nc))                  # 큐에 해당 위치 담아주고
                    sol.append(room[nr][nc])                # 방문할 예정이니까 방문 리스트에도 담아줌
                    visited[nr][nc] = 1                     # 방문 예정이니까 미리 방문 체크
    return min(sol), len(sol)                               # min(sol): 방문한 방 중 가장 번호가 작은 방, len(sol): 방문한 방의 개수

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    room_num, move = n*n, 0                                 # n*n만큼의 방의 개수가 있으므로 방번호 최대값으로 초기화
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                temp_num, temp_move = bfs(r, c)
                '''move <= temp_move로 하면 안되는 이유
                -> move < temp_move이면 무조건 새로 살펴본 값으로 변경해야 함
                (move < temp_move) or (move == temp_move and room_num > temp_num)인듯'''
                if move < temp_move or move == temp_move and room_num > temp_num:
                    room_num, move = temp_num, temp_move

    print('#{} {} {}'.format(tc, room_num, move))