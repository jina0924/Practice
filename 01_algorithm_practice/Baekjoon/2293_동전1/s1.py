# 백준 2293번 동전1

import sys
sys.stdin = open('input.txt')


def func(res, i):
    global cnt
    if i >= n:
        return
    res %= coin[i]
    if res == 0:
        cnt += 1
    elif res < coin[i]:
        func(res, i + 1)
    func(res + coin[i], i + 1)


n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0
func(k, 0)
print(cnt)
