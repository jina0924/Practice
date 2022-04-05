# SWEA 5205. 퀵 정렬

import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return [*sorted_left, pivot, *sorted_right]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(data)[N//2]}')