# SWEA 2117. 홍 방범 서비스

import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 도시의 크기, M: 하나의 집을 지불할 수 있는 비용
    town = [list(map(int, input().split())) for _ in range(N)]
    ans = 1                             # k가 1일 때 제공받을 수 있는 가구 수
    k = 2                               # k가 1일 때는 무조건 1가구이므로 2부터 시작
    while k <= N+1:                     # 영역의 크기가 도시를 다 덮을때까지
        cost = k**2 + (k-1)**2
        for sr in range(N):             # 방범 중앙지 위치
            for sc in range(N):
                cnt = 0                 # 가구 수 담을 변수
                for r in range(N):
                    for c in range(N):
                        if abs(sr - r) + abs(sc - c) < k and town[r][c]:    # 중앙으로부터 k 미만 떨어져있는 가구 세어줌
                            cnt += 1
                if cost <= cnt * M:     # 만약 손해를 보지 않을 때
                    if ans < cnt:       # 가구 수가 기존 값보다 많다면 갱신
                        ans = cnt
        k += 1                          # k 면전 1씩 늘려감

    print('#{} {}'.format(tc, ans))

# SWEA 2117. 홍 방범 서비스

import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 도시의 크기, M: 하나의 집을 지불할 수 있는 비용
    town = [list(map(int, input().split())) for _ in range(N)]
    ans = 1                             # k가 1일 때 제공받을 수 있는 가구 수
    k = 2                               # k가 1일 때는 무조건 1가구이므로 2부터 시작
    while k <= N+1:                     # 영역의 크기가 도시를 다 덮을때까지
        cost = k**2 + (k-1)**2
        for sr in range(N):             # 방범 중앙지 위치
            for sc in range(N):
                cnt = 0                 # 가구 수 담을 변수
                for r in range(N):
                    for c in range(N):
                        if abs(sr - r) + abs(sc - c) < k and town[r][c]:    # 중앙으로부터 k 미만 떨어져있는 가구 세어줌
                            cnt += 1
                if cost <= cnt * M:     # 만약 손해를 보지 않을 때
                    if ans < cnt:       # 가구 수가 기존 값보다 많다면 갱신
                        ans = cnt
        k += 1                          # k 면전 1씩 늘려감

    print('#{} {}'.format(tc, ans))

