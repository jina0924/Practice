# 백준 6603번 로또

import sys
sys.stdin = open('input.txt')


def lotto(n):
    if n >= 6:
        print(*nums)
        return
    for i in range(k):
        if not picked[i] and nums[n-1] < s[i]:
            nums[n] = s[i]
            picked[i] = 1
            lotto(n+1)
            nums[n] = 0
            picked[i] = 0

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    nums = [0] * 6
    picked = [0] * k
    lotto(0)
    print()
