# SWEA 5688. 세제곱근을 찾아라

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cbrt = round(pow(N, 1/3))       # 소수점 처리하기 위해 반올림해줌
    if cbrt**3 == N:                # 반올림한 값을 세제곱했을 때 N값이 나온다면
        ans = cbrt                  # 해당 정수가 세제곱근
    else:
        ans = -1
    print('#{} {}'.format(tc, ans))