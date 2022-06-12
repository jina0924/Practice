# SWEA 5205. 퀵 정렬

import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):             # 배열을 나눌 기준을 고르는 함수
    pivot = arr[start]                      # 기준은 배열의 첫 번째 값
    left, right = start + 1, end            # 양쪽에서 원하는 값 나올때까지 좁혀감
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:     # 피봇보다 큰 값을 만날때까지 반복
            left += 1
        while left <= right and pivot <= arr[right]:    # 피봇보다 작은 값 만날때까지 반복
            right -= 1
        if right < left:                    # 모든 반복을 다 돌았을 때 왼쪽에 있는 값들이 오른쪽에 있는 값들보다 작을 때
            done = True                     # 정렬 끝난 상태
        else:                   # left와 right가 아직 교차되지 않았다면 아직 피봇이 자리할 위치 찾지 못함
            arr[left], arr[right] = arr[right], arr[left]   # 왼쪽값과 오른쪽 값 바꿔주어 피봇이 자리할 수 있도록 만들어줌
    arr[start], arr[right] = arr[right], arr[start]
    return right                # right가 새로운 피봇값이 됨


def quick_sort(arr, start, end):
    if start < end:                         # start와 end가 같지 않다면 아직 정렬되지 않은 상태 있음
        pivot = partition(arr, start, end)  # 자리 잡은 기준값
        quick_sort(arr, start, pivot - 1)   # 처음 값 부터 기준값 전까지 정렬
        quick_sort(arr, pivot + 1, end)     # 기준 값 이후부터 끝 값까지 정렬
    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(data, 0, len(data) - 1)[N//2]}')