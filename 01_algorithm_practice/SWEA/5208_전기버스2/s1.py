# SWEA 5208. 전기 버스2

import sys
sys.stdin = open('input.txt')


def bus(station):
    global cnt, ans
    if cnt >= ans:                  # 가지치기: 지금 살펴본 교환 횟수가 최소 횟수보다 크다면 되돌아가기
        return

    for b in range(data[station], 0, -1):   # 현재 배터리로 갈 수 있는 정류장 살펴보기
        if station + b >= N:        # 만약 지금 배터리로 종점 이상 갈 수 있다면
            if cnt < ans:           # 배터리 교환 횟수 갱신해줌
                ans = cnt
            return
        cnt += 1                    # 배터리 교체해주고
        bus(station + b)            # 다음 정류장으로 감
        cnt -= 1                    # 배터리 교체횟수 되돌리기


T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]                 # N: 정류장 수
    cnt, ans = 0, 99            # cnt: 배터리 교환횟수, ans: 최소 교환 횟수
    bus(1)                      # 1번 정류장부터 시작
    print(f'#{tc} {ans}')