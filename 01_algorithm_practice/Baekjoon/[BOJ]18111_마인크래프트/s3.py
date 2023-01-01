# 백준 18111번 마인크래프트

import sys
sys.stdin = open('input4.txt')
input = sys.stdin.readline


def flatten(height):
    global ans, top
    lack, overflow = 0, 0

    for r in range(N):
        for c in range(M):
            if ground[r][c] > height:
                lack += ground[r][c] - height
            elif ground[r][c] < height:
                overflow += height - ground[r][c]
    if B + lack - overflow < 0:
        return
    if lack * 2 + overflow <= ans:
        ans = lack * 2 + overflow
        top = height


N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
ans, top = 987987987, 0
for h in range(257):
    flatten(h)
print(ans, top)