# SWEA 5207. 이진 탐색

import sys
sys.stdin = open('input.txt')


def binary_search(arr, num):
    start, end = 0, N - 1               # start: 살펴보는 구간의 시작, end: 구간의 끝
    left_right = 0                      # 왼쪽 구간 보면 1, 오른쪽 구간 보면 2로 저장할 것
    while start <= end:                 # 구간을 최대한 좁혀서 1개만 볼 때까지
        mid = (start + end) // 2        # mid: 구간 중심 원소의 인덱스
        if arr[mid] == num:             # 만약 중심 원소값이 찾고자 하는 값이라면
            return 1                    # 바로 1 반환
        elif arr[mid] < num:            # 중앙값이 현재 살펴보는 값보다 작다면
            start = mid + 1             # 오른쪽 구간 살펴봐야함
            if left_right == 2:         # 만약 이전에 오른쪽 구간 살펴봤었다면
                return 0                # 틀렸다
            left_right = 2              # return 안만났다면 오른쪽 구간 살폈다는 표시 해주기
        elif arr[mid] > num:            # 위와 동일
            end = mid - 1
            if left_right == 1:
                return 0
            left_right = 1
    return 0                            # 구간을 최대한 좁혀도 값을 못찾았다면 그 값 없으니까 0 반환


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        ans += binary_search(A, b)
    print(f'#{tc} {ans}')