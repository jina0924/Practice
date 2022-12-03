# 백준 18113번 그르다 김가놈

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N, K, M = map(int, input().split())     # N: 김밥의 개수, K: 꼬다리의 길이, M: 김밥 조각의 최소 개수
P = -1
arr = []

# 김밥 꼬다리 자르기
for _ in range(N):
    kimbab = int(input())
    if kimbab > 2 * K:
        arr.append(kimbab - 2 * K)
    elif K < kimbab < 2 * K:
        arr.append(kimbab - K)

# 손질하고 남은 김밥이 없다면 -1 출력
if not len(arr):
    print(P)
    sys.exit(0)                             # EXIT_SUCCESS (exit(1) : EXIT_FAILURE)

l, r = 1, max(arr)                      # 공약수 찾기 위한 값
while l <= r:
    m = (l + r) // 2                    # m: 김밥 조각 길이
    total = sum([kimbab//m for kimbab in arr])
    if total < M:                       # 개수가 모자라다면 조각 길이 줄이기
        r = m - 1
    else:                               # 개수가 최소 M개라면
        l = m + 1                       # 조각 길이 늘려보고
        P = m                           # 현재 길이 저장해두기

print(P)