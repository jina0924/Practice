# SWEA 5249. 최소 신장 트리 - Kruskal

import sys
sys.stdin = open('input.txt')


def find_set(x):                                        # 대표 원소 찾기
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):                                        # 그룹 합치기
    p[find_set(y)] = find_set(x)


def kruskal():
    global ans
    edge_cnt = idx = 0                                  # edge_cnt: 간선 선택 개수, idx: 간선 정보 인덱스

    while edge_cnt < V:                                 # 신장 트리: (정점의 개수 - 간선의 개수) = 1
        x, y = edges[idx][0], edges[idx][1]

        if find_set(x) != find_set(y):                  # 서로 다른 그룹이라면(사이클이 아니라면)
            union(x, y)                                 # 그룹 합치기
            edge_cnt += 1                               # 간선 선택했으므로 개수 1 올려줌
            ans += edges[idx][2]                        # 가중치 더해줌
        idx += 1                                        # 간선 선택 여부에 상관없이 다음 간선 보기 위해 인덱스 값 1 올려줌

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())                    # V: 노드 번호, E: 간선의 개수
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])                      # 가중치를 기준으로 오름차순 정렬
    p = list(range(V+1))                                # 상호배타집합
    ans = 0                                             # 최소 신장트리의 가중치 합
    kruskal()
    print(f'#{tc} {ans}')