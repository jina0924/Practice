# 백준 2293번 동전1

import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
idx = cnt = 0
while idx < n:
    k -= coin[idx]
    if k == 0:
        cnt += 1
        k += coin[idx]
        idx += 1
    elif k < coin[idx]:
        idx += 1
