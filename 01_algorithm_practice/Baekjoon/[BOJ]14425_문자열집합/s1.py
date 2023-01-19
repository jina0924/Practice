# 백준 14425번 문자열 집합

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
words = set()
for _ in range(N):
    words.add(input().rstrip())
cnt = 0
for _ in range(M):
    word = input().rstrip()
    if word in words:
        cnt += 1
print(cnt)