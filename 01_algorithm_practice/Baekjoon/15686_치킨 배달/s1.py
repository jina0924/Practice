# 백준 15686번 15686_치킨 배달

import sys
sys.stdin = open('input4.txt')
from itertools import combinations


def chicken_road(stores):
    total = 0                           # 치킨 거리 총 합을 담을 변수
    for h in house:                     # 각 집에서 치킨집의 거리 계산해서 작은 값 선택할 것
        minD = 100                      # 거리의 최소값을 갱신할 변수
        for store in stores:            # 치킨집을 순회하면서
            distance = abs(h[0] - store[0]) + abs(h[1] - store[1])      # 집과 치킨집의 거리 계산
            if minD > distance:         # 만약 지금 본 치킨집이 더 가깝다면
                minD = distance         # 치킨 거리 갱신
        total += minD                   # 각 집마다 구해진 치킨 거리 더해줌
    return total


N, M = map(int, input().split())        # N: 도시 한 변의 길이, M: 치킨집의 개수의 최대값
data = [list(map(int, input().split())) for _ in range(N)]      # 0: 빈 칸, 1: 집, 2: 치킨 집
house = []                              # 집의 좌표들
chicken = []                            # 치킨집의 좌표들
for r in range(N):
    for c in range(N):
        if data[r][c] == 1:
            house.append((r, c))
        elif data[r][c] == 2:
            chicken.append((r, c))
ans = 1300
for com in combinations(chicken, M):        # M개의 치킨집을 골라서
    result = chicken_road(com)              # 치킨 거리 계산
    if ans > result:                        # 만약 더 적은 값의 치킨 거리가 나왔다면 갱신
        ans = result
print(ans)