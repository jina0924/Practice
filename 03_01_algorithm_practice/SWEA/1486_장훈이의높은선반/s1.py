# SWEA 1486

import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, b = map(int, input().split())            # n: 점원의 수 / b: 선반의 높이
    height = list(map(int, input().split()))    # 점원들이 키 배열
    tower = []                                  # 선반보다 높은 탑을 담을 리스트
    for i in range(1, n+1):                     # 탑을 쌓을 인원수
        for c in combinations(height, i):       # 해당 인원수만큼 나올 수 있는 조합의 수
            if sum(c) >= b:                     # 만약 선반보다 높거나 같은 높이의 탑이 쌓인다면
                tower.append(sum(c) - b)        # tower에 더해주고
    print('#{} {}'.format(tc, min(tower)))      # 그 중 가장 작은 값을 출력

