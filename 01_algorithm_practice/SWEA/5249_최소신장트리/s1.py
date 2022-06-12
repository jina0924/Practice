# SWEA 5249. 최소 신장 트리 - Prim

import sys
sys.stdin = open('input.txt')
import heapq


def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, 0))                        # (가중치, 정점)을 heap에 넣음
    while heap:
        weight, v = heapq.heappop(heap)
        if not visited[v]:                              # 방문하지 않았다면
            ans += weight                               # 가중치를 더해주고
            visited[v] = 1                              # 방문체크 해줌
            for i in range(V+1):                        # 모든 정점을 반복하면서
                if G[v][i] and not visited[i]:          # 현재 정점과 연결되어있고 아직 방문하지 않은 곳이라면
                    heapq.heappush(heap, (G[v][i], i))      # heap에 넣어줌

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())                    # V: 노드 번호, E: 간선의 개수
    G = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)                               # 방문 체크 배열
    for _ in range(E):
        n1, n2, w = map(int, input().split())           # n1, n2: 간선의 양 끝 노드 / w: 가중치
        G[n1][n2] = G[n2][n1] = w
    ans = 0                                             # 최소 신장트리의 가중치 합
    prim()
    print(f'#{tc} {ans}')