# 백준 14719번 빗물

import sys
sys.stdin = open('input3.txt')

H, W = map(int, input().split())
data = [[0] * W for _ in range(H)]
blocks = list(map(int, input().split()))
for c in range(W):
    for h in range(blocks[c]):
        data[h][c] = 1

ans = 0
for r in range(H):
    c = 0
    while c < W:
        if data[r][c] and c < W - 1:
            cnt = 0
            start = c + 1
            while start < W:
                if start == W - 1 and data[r][start] == 0:
                    c = start
                    break
                if data[r][start] == 0:
                    start += 1
                    cnt += 1
                else:
                    ans += cnt
                    c = start
                    break
        else:
            c += 1
print(ans)