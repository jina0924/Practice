# 백준 1182번 부분수열의 합

import sys
sys.stdin = open('input2.txt')


def ssum(n, result):
    global cnt
    if n >= N:
        if result == S and sum(picked):
            cnt += 1
        return
    picked[n] = 1
    ssum(n+1, result + data[n])
    picked[n] = 0
    ssum(n+1, result)



N, S = map(int, input().split())
data = list(map(int, input().split()))
picked = [0] * N
cnt = 0
ssum(0, 0)
print(cnt)