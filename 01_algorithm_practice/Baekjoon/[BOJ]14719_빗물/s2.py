# 백준 14719번 빗물

import sys
sys.stdin = open('input3.txt')

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
for h in range(H):
    nc, cnt = False, 0
    for c in range(W):
        if blocks[c] >= h:
            nc = True
            if cnt > 0:
                ans += cnt
                cnt = 0
        else:
            if nc:
                cnt += 1

print(ans)