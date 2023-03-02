# 백준 1920번 수 찾기 - 이진탐색

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
checkList = list(map(int, input().split()))
for num in checkList:
    left, right = 0, N - 1
    isIn = False
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            print(1)
            isIn = True
            break
        elif arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
    if not isIn:
        print(0)
