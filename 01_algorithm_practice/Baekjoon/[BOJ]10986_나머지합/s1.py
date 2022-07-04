# 백준 10986번 나머지 합

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
data = list(map(int, input().split()))

for i in range(N):
    data[i] %= M

result = [data[0]]
i, cnt = 1, 0
if data[0] == 0:
    cnt += 1
while i < N:
    if data[i] == 0:
        cnt += 1
    temp = []
    for res in result:
        new_res = (res + data[i]) % M
        if new_res == 0:
            cnt += 1
        temp.append(new_res)
    result += temp
    i += 1
print(cnt)