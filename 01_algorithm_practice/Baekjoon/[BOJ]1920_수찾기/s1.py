# 백준 1920번 수 찾기

import sys
sys.stdin = open('input.txt')

N = int(input())
nums = set(map(int, input().split()))
M = int(input())
checkList = list(map(int, input().split()))
for i in range(M):
    if checkList[i] in nums:
        print(1)
    else:
        print(0)