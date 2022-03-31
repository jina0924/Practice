# SWEA 10726. 이진수 표현

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 비트, M: 정수
    # Mbin = [0] * N                      # N 비트만큼 담을 리스트
    pos = N - 1                         # 마지막부터 N비트까지 가리킬 인덱스
    ans = 'ON'                          # N비트 모두 1로 켜져있는지 확인할 변수
    while pos >= 0:                     # N비트 모두 살펴볼 때까지 반복
        if M % 2:                       # 만약 2로 나눴을 때 나머지가 1이라면 = 비트가 1로 켜질 수 있다면
            # Mbin[pos] = 1               # Mbin에 해당 자리 켜주고
            M //= 2                     # M을 2로 나눈 몫으로 할당
            pos -= 1                    # 현재보다 앞자리 인덱스로 옮김
        else:                           # 만약 나머지가 0이라면 = 앞으로 더 비트 살펴볼 필요 없음
            ans = 'OFF'                 # 켜져있지 않음을 나타내고
            break                       # 반복 끝냄

    print(f'#{tc} {ans}')