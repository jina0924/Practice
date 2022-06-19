# 백준 2293번 동전1

import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
idx = cnt = 0
