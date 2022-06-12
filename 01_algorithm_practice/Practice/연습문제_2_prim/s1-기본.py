"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합
"""

def prim():
    for _ in range(V):                                          # 모든 정점이 MST에 포함될 때까지 반복 (마지막 요소 선택 여부)
        min_idx = -1           
        min_value = 987654321
    
        #1. 최솟값 찾기
        for i in range(V+1):                                    # key가 최솟값을 갖는 인덱스 찾기
            if not visited[i] and key[i] < min_value:           # i번째 정점을 선택하지 않았고 선택하지 않은 정점 중에서 최솟값 찾기
                min_idx = i                                     # 최솟값 인덱스 초기화
                min_value = key[i]                              # 최솟값 초기화
        visited[min_idx] = 1                                    # MST에 속하는 정점을 체크

        #2. 해당 값으로부터 연결된 정점 가중치 갱신
        for i in range(V+1):                                    # min_idx와 연결된 인접 행렬 돌면서 (갱신할 수 있다면 가중치 갱신)
            if not visited[i] and G[min_idx][i] < key[i]:       # 정점 선택 안했고 해당 가중치가 key의 요소보다 작으면 (== 더 적은 비용으로 MST에 연결되면)
                key[i] = G[min_idx][i]
        print(key)
    return sum(key)

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())                                # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1
G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]       # 임의의 큰 값으로 초기화
key = [987654321] * (V+1)                                       # 갱신된 최솟값 가중치(처음은 임의의 큰 값으로 초기화) -> MST에 속하는데 포함되는 비용(가중치)
key[0] = 0                                                      # 0번 정점에서 시작 (시작점은 임의로 선택 가능) -> 처음은 가중치가 0
visited = [0] * (V+1)                                           # MST에 포함되는지 여부 체크 -> 현재 정점을 선택했는지 여부 체크
for i in range(E):
    start, end, W = map(int, input().split())                   # start, end, W: 가중치
    G[start][end] = W                                           # 무향 그래프이므로 양쪽에 모두 가중치 체크
    G[end][start] = W
print(prim())                                                   # 22