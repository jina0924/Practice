# SWEA 2814. 최장 경로

import sys
sys.stdin = open('input.txt')


def dfs(v):
    global cnt, ans

    for i in range(1, N+1):
        if Graph[v][i] and not visited[i]:      # 인접한 정점이고 아직 방문하지 않았다면
            cnt += 1                            # 경로 길이 더해주고
            visited[i] = 1                      # 방문(예정)표시해주고
            dfs(i)                              # 방문하러 감
            cnt -= 1                            # 다른 곳 방문하기 위해 값 초기화
            visited[i] = 0
    else:                                       # for문을 다 돌아도 인접한 곳이 없다 = 경로의 끝
        if ans < cnt:                           # 최대값으로 갱신해주기
            ans = cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())            # N: 정점의 개수, M: 간선의 개수
    Graph = [[0] * (N+2) for _ in range(N+2)]   # 정점이 1부터 시작하니까 N개만큼 인덱스 접근하기 위해 N+2크기
    for _ in range(M):                          # 무방향 그래프
        v1, v2 = map(int, input().split())
        Graph[v1][v2] = 1
        Graph[v2][v1] = 1
    visited = [0] * (N+2)                       # 방문표시를 위한 배열
    cnt = 1                                     # 매번 체크할 경로 길이
    ans = 1                                     # 최장 경로 길이
    for i in range(1, N+1):                     # 1 ~ N 정점마다 출발
        visited[i] = 1                          # 출발지 방문표시해줌
        dfs(i)                                  # 해당 위치에서 인접한 정점으로 출발
        visited[i] = 0                          # 출발지 변경을 위해 초기화
    print(f'#{tc} {ans}')