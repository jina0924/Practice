# SWEA 5248. 그룹 나누기

import sys
sys.stdin = open('input.txt')


def find_set(x):                            # 대표 원소 찾기
    while x != group[x]:
        x = group[x]
    return x


def union(x, y):                            # 그룹 합치기
    # x, y = find_set(x), find_set(y)
    group[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 출석 번호, M: 신청서 개수
    data = list(map(int, input().split()))      # 지목한 번호
    group = list(range(N+1))                # 인덱스 컨트롤을 위해 N+1까지
    for i in range(M):
        a, b = data[i*2], data[i*2+1]
        union(a, b)                         # b가 a를 지목했으므로 b의 대표를 a의 대표값으로 변경
    ans = set()
    for i in range(1, N+1):
        ans.add(find_set(group[i]))
    print(f'#{tc} {len(ans)}')