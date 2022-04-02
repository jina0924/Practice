# SWEA 1952. 수영장

import sys
sys.stdin = open('input.txt')


def charge(month):
    if month <= 1:                                          # 맨 뒤에서부터 살펴봤으므로 1월이 마지막으로 살펴볼 순서
        if d * plan[month] > m1:
            return m1
        return d * plan[month]
    else:
        if d * plan[month] > m1:                            # 이번 달 이용 요금 중 적은 값 찾기
            month_charge = m1
        else:
            month_charge = d * plan[month]
        # 저번 달 이용요금 + 이번 달 이용요금이 3달 전 이용요금 + 세달 이용권보다 크다면 세달 이용권 사는게 이득
        '''
        2월 달이 경우 charge(month-3)에서 month-3이 -1이 되는데
        함수 맨 첫번째 조건을 if month <= 1로 둬서
        plan[month]가 plan[-1]을 찾게 된다.
        파이썬에선 음수 인덱싱이 가능해서 원하는 결과값이 나온 것 같다'''
        if charge(month-1) + month_charge > charge(month-3) + m3:
            return charge(month-3) + m3
        return charge(month-1) + month_charge               # 위의 if문에서 return을 만나지 않았다 = 세달 이용권이 더 비싸다


T = int(input())


for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())                # d: 1일 이용권, m1: 한달 이용권, m3: 세달 이용권, y: 1년 이용권
    plan = [0] + list(map(int, input().split())) + [0, 0]   # 인덱스 값으로 각 달에 접근하기 위해 0으로 패딩 줌
    ans = charge(14)                                        # 12월에 쓸 3달 이용권 살펴보기 위해 14번째 부터 함수 시작
    if ans > y:                                             # 함수에서 나온 결과값이 1년 이용권보다 비싸다면
        ans = y                                             # 1년 이용권으로 바꿈
    print('#{} {}'.format(tc, ans))

