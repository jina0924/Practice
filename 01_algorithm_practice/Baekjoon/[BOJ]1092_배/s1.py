# 백준 1092번 배

import sys
sys.stdin = open('input4.txt')

N = int(input())                            # N: 크레인 수
crane = sorted(list(map(int, input().split())))     # 크레인의 무게 제한
M = int(input())                            # M: 박스 수
box = sorted(list(map(int, input().split())))       # 각 박스의 무게
i, j = N-1, M-1
cnt = 0
while j >= 0:
    if box[j] <= crane[i]:
        box[j] = 0
        j -= 1
    i -= 1
    if i < 0 or j < 0:
        i = N-1
        cnt += 1
print(cnt)