# SWEA 1953. 탈주범 검거

import sys
from collections import deque
sys.stdin = open('input.txt')

# 각 터널 별로 갈 수 있는 방향
tunnel = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}

def spot(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1               # 매개변수로 받은 위치 방문 표시
    cnt = 1                         # 탈주범이 갈 수 있는 위치 개수를 담을 변수

    while queue:
        r, c = queue.popleft()      # 큐에서 꺼낸 값이 현재 위치
        if visited[r][c] == l:      # 현재 위치를 방문한 시간이 최초로 탈출 후 소요 시간과 같다면
            return cnt              # cnt값 반환하고 함수 끝냄
        for d in tunnel.get(underground[r][c]): # 현재 위치에 있는 터널에서 갈 수 있는 방향별로 반복
            nr, nc = r + d[0], c + d[1]         # 현재 위치에서 갈 수 있는 새로운 위치
            # 지하 지도 안에 있고 & 그 위치가 터널이고 & 아직 방문하지 않은 곳이면서
            if 0 <= nr < n and 0 <= nc < m and underground[nr][nc] and not visited[nr][nc]:
                # 새롭게 살펴보는 위치의 터널이 현재 위치와 이어져 있는지 살펴보기
                for d in tunnel.get(underground[nr][nc]):
                    if r == nr + d[0] and c == nc + d[1]:
                        queue.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1     # 어차피 갈 곳이니까 미리 방문 표시
                        cnt += 1                                # 큐에 담은 만큼 cnt값 올려주기
    return cnt

T = int(input())

for tc in range(1, T+1):
    # n: 지도의 세로 크기, m: 가로 크기, r: 맨홀 위치의 세로 위치, c: 가로 위치, l: 탈출 후 소요 시간
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ans = spot(r, c)
    print('#{} {}'.format(tc, ans))

