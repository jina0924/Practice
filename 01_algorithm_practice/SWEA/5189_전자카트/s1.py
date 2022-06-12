# 5189. 전자카트

import sys
sys.stdin = open('input.txt')


def dfs(r, c, battery):
    global ans
    r = c                                       # 함수로 넘겨받은 c = 다음에 방문할 r값
    if sum(visited) == N:                       # 만약 모두 방문했다면 visited의 모든 요소가 1로 채워짐
        battery += data[r][0]                   # 마지막 위치에서 사무실로 오는 배터리량 더해줌
        if ans > battery:                       # 현재 살펴본 배터리 소비량이 원래 값보다 더 작다면 갱신
            ans = battery

    for i in range(N):                          # 관리구역을 돌아보면서
        if not visited[i]:                      # 아직 방문하지 않은 곳이라면
            visited[i] = 1                      # 방문표시하고
            dfs(r, i, battery + data[r][i])     # 해당 위치까지 가는 배터리 사용량을 더해서 가봄
            visited[i] = 0                      # 방문 순서 바꾸기 위해 방문 표시 초기화

T = int(input())

for tc in range(1, T + 1):
    N = int(input())                            # N: (사무실 + 골프장 관리구역)의 개수
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N                           # 각 위치 방문표시를 할 배열
    ans = 1000                                  # 최소 배터리 소비량을 담을 변수
    visited[0] = 1                              # 사무실에서 시작하므로 사무실 위치 방문 표시
    dfs(0, 0, 0)                                # 사무실에서 출발
    print(f'#{tc} {ans}')