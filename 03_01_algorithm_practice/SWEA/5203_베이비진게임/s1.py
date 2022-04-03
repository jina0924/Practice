# SWEA 5203. 베이비진 게임

import sys
sys.stdin = open('input.txt')

T = int(input())


def baby_gin(i):
    global ans
    while i < 6:                                # 모두 6장의 카드를 나눠 가질 때까지 반복
        p1.append(cards[i*2])
        p1.sort()                               # 새 카드 담았으니까 정렬해줌
        for j in range(len(p1)-2):              # 마지막에서 세 번째카드까지 시작점 될 수 있음
            if p1.count(p1[j]) >= 3:            # 만약 지금 카드가 3장 이상이라면 triplet
                ans = 1                         # 승자 결정남
                return                          # 함수 끝냄
            if p1[j] + 1 in p1 and p1[j] + 2 in p1: # 정렬되어 있으므로 -> 지금 숫자부터 연속으로 3개 있으면
                ans = 1                         # 승자 결정남
                return
        p2.append(cards[i*2+1])
        p2.sort()
        for j in range(len(p2)-2):
            if p2.count(p2[j]) >= 3:
                ans = 2
                return
            if p2[j] + 1 in p2 and p2[j] + 2 in p2:
                ans = 2
                return
        i += 1                                  # return을 만나지 못했다면 아직 승패 갈리지 않았으므로 카드 한장씩 더 나눠가짐
    return                                      # while문에서 return 만나지 못함 = 무승부


for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []                                 # 플레이어1의 카드
    p2 = []                                 # 플레이어2의 카드
    for idx in range(2):                    # 우선 2장씩 나눠 가짐(2장일 땐 run이나 triplet 판별 못하니까)
        p1.append(cards[idx * 2])
        p2.append(cards[idx * 2 + 1])
    ans = 0                                 # 승자 담을 변수(초기값 = 무승부일때)
    baby_gin(2)                             # 세 번째 카드부터 담으러 감


    print(f'#{tc} {ans}')