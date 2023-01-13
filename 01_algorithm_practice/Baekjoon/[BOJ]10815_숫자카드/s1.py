# 백준 10815번 숫자 카드

import sys
sys.stdin = open('input.txt')

N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
data = list(map(int ,input().split()))
for num in data:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')