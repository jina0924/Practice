# SWEA 7465. 창용 마을 무리의 개수

import sys
sys.stdin = open('input.txt')


def find_set(x):
    while x != p[x]:                            # 최종 대표 원소를 만날 때 까지 거슬러 올라가기
        x = p[x]
    return x

def union(x, y):                                # 그룹 합치기
    p[find_set(y)] = find_set(x)                # x의 대표 원소가 y의 대표원소가 되도록 만듦

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())            # N: 마을 사람 수, M: 관계 수
    p = list(range(N+1))                        # 상호 배타 집합을 표현할 배열
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for i in range(N+1):                        # 지금까지 담긴 p 배열에서 같은 그룹이 있는지 살펴보기
        p[i] = find_set(i)
    print(f'#{tc} {len(set(p))-1}')             # set으로 만들고 0을 제거하기 위해 1 빼줌