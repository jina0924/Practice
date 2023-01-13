# 백준 1269번 대칭 차집합

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection = A & B
print(N + M - len(intersection) * 2)