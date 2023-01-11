# 백준 10816 숫자 카드 2

import sys
sys.stdin = open('input.txt')
from collections import defaultdict


N = int(input())
cards = defaultdict(int)
temp = list(map(int, input().split()))
for n in range(N):
    cards[temp[n]] += 1
# print(cards)
# cards = set(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))
for num in data:
    if num in cards.keys():
        print(cards[num], end=' ')
    else:
        print(0, end=' ')