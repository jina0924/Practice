# 백준 10807번 개수 세기

import sys
sys.stdin = open('input2.txt')

N = int(input())
data = list(map(int, input().split()))
v = int(input())

cnt = 0
for num in data:
    if num == v:
        cnt += 1
print(cnt)
# print(data.count(v))