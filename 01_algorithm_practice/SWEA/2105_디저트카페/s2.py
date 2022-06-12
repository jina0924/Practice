# SWEA 2105. 디저트 카페 - set사용

import sys
sys.stdin = open('input.txt')

delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]    # 우하, 좌하, 좌상, 우상 으로 움직임


def tour(r, c, d, data):
    global ans

    nr, nc = r + delta[d][0], c + delta[d][1]

    if nr == start_r and nc == start_c:         # 만약 새롭게 살펴보는 위치가 처음 출발 위치랑 같다면
        if ans < len(data):                     # 투어한 디저트 종류가 지난번보다 많다면
            ans = len(data)                     # 현재 개수로 갱신해줌
        return

    # 새로 살펴본 위치가 범위를 벗어나거나 이미 살펴본 디저트라면 투어돌지 않음
    if nr >= N or nr < 0 or nc >= N or nc < 0 or cafe[nr][nc] in data:
        return


    tour(nr, nc, d, data | {cafe[nr][nc]})
    if d < 3:                                   # 만약 마지막으로 방향 틀지 않았다면 방향 틀어서 한번 더 살펴봐줌
        tour(nr, nc, d+1, data | {cafe[nr][nc]})


T = int(input())

for tc in range(1, T+1):
    N = int(input())                        # N: 지역의 한 변의 길이
    cafe = [list(map(int, input().split())) for _ in range(N)]
    ans = -1                                # 디저트를 먹을 수 없는 경우를 초기값으로 설정
    for r in range(N-2):                    # 최소한의 사각형 크기 고려해서 범위 지정
        for c in range(1, N-1):
            start_r, start_c = r, c         # 투어 끝을 살펴보기 위해 현재 위치 저장
            tour(r, c, 0, {cafe[r][c]})     # 현재 위치부터 카페투어 시작
    print('#{} {}'.format(tc, ans))

