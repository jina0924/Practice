# 백준 18111번 마인크래프트

import sys
sys.stdin = open('input1.txt')

N, M, B = map(int, input().split())
ground = []
top = B
for r in range(N):
    data = list(map(int, input().split()))
    for c in range(M):
        if data[c] < top:
            top = data[c]
    ground.append(data)
print(ground, top)