# 백준 15961번 회전초밥

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi_cnt = [0] * (d + 1)
sushi_cnt[c] += 1
belt = [int(input()) for _ in range(N)]
start, end = 0, 0
total = k + 1
while end < k:
    sushi_cnt[belt[end]] += 1
    if sushi_cnt[belt[end]] >= 2:
        total -= 1
    end += 1
ans = total
while start < N:
    sushi_cnt[belt[start]] -= 1
    start += 1
    if end < N - 1:
        end += 1
    else:
        end = 0
    sushi_cnt[belt[end]] += 1
    if sushi_cnt[belt[end]] >= 2:
        total -= 1
    ans = max(ans, total)
print(ans)