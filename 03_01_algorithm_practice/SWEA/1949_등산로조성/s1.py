# SWEA 1949. 등산로 조성

import sys
sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # 상, 하, 좌, 우
def contruct(r, c, cnt):
    global cut, ans

    for d in range(4):                          # 상하좌우 살펴보면서
        nr, nc = r + delta[d][0], c + delta[d][1]   # 새롭게 살펴볼 위치가
        if 0 <= nr < N and 0 <= nc < N:         # 부지 안에 있고
            # 현재 위치보다 낮으면서 아직 방문하지 않았다면
            if data[nr][nc] < data[r][c] and not visited[nr][nc]:
                visited[nr][nc] = 1             # 방문 표시 해주고
                contruct(nr, nc, cnt + 1)       # 새 위치에서 다시 사방 살피러 감
                visited[nr][nc] = 0             # vistied 빨아쓰기
            elif cut:                           # 만약 깎을 기회가 남아있다면
                for k in range(1, K+1):         # 1 ~ 최대 깊이 만큼 깎아보기
                    # 만약 깎을 위치가 현재 위치보다 낮고 아직 방문하지 않았다면
                    if data[nr][nc] - k < data[r][c] and not visited[nr][nc]:
                        data[nr][nc] -= k       # 깎아버리고
                        cut = 0                 # 깎을 기회 0으로 만듦
                        visited[nr][nc] = 1     # 방문표시해주고
                        contruct(nr, nc, cnt + 1)   # 깎아준 새 위치의 사방 살피러 감
                        visited[nr][nc] = 0     # 다 살피고 왔다면 방문표시 초기화해주고
                        data[nr][nc] += k       # 다른 등산로에서 원래 값으로 살펴보기 위해 원래 값으로 초기화해주고
                        cut = 1                 # 깎을 기회도 살려놓음
    else:                                       # for-else: 사방 다 살펴봐도 더 갈 길이 없다 = 등산로 다 봤다
        if ans < cnt:                           # ans가 현재 등산로 길이보다 작은 값이라면 갱신
            ans = cnt
        return


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())        # N: 지도의 한 변의 길이, K: 최대 공사 가능 깊이
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    top = max(data[0])                      # top: 등산로 가장 높은 봉우리 담을 변수
    cut = 1                                 # 단 한번 깎을 수 있음을 나타낼 변수
    for i in range(1, N):                   # 가장 높은 봉우리 값 찾음
        if top < max(data[i]):
            top = max(data[i])
    ans = 0                                 # 가장 긴 등산로 길이를 담을 변수(0으로 초기화)
    for r in range(N):
        for c in range(N):
            if data[r][c] == top:           # 가장 높은 봉우리라면
                visited[r][c] = 1           # 우선 방문 표시하고
                contruct(r, c, 1)           # 등산로 조성하러 감
                visited[r][c] = 0           # visited 빨아쓰기 위해 0으로 다시 초기화
    print(f'#{tc} {ans}')