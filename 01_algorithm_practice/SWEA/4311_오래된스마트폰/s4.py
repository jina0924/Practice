# SWEA 4311. 오래된 스마트폰

import sys
sys.stdin = open('input.txt')

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    num1 = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    W = int(input())
    numbers = [0] * 1000
    print(f'#{tc} {touch()}')