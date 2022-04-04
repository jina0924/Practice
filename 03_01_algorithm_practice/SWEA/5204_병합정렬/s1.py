# SWEA 5204. 병합 정렬

import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    if len(left) == 0:      # left의 요소가 없다 = right에는 요소가 1개 뿐이다 = 정렬 필요 x
        return right

    if len(right) == 0:
        return left

    sorted_list = []
    L = R = 0
    if left[-1] > right[-1]:                            # 만약 왼쪽 마지막 값이 오른쪽 마지막 값보다 크다면
        cnt += 1                                        # 경우의 수 1 올려줌
    while len(sorted_list) < len(left) + len(right):    # left랑 right가 모두 병합될 때까지
        if left[L] <= right[R]:                         # 만약 left의 요소가 right의 요소보다 작다면
            sorted_list.append(left[L])
            L += 1

        else:
            sorted_list.append(right[R])
            R += 1

        if L == len(left):                              # 만약 왼쪽의 모든 요소를 다 정렬된 리스트에 넣었다면
            sorted_list += right[R:]                    # 오른쪽에 남은 모든 요소 몽땅 털어 넣음
            break                                       # 더이상 while문 반복하지 않기 위해 break

        if R == len(right):
            sorted_list += left[L:]
            break

    return sorted_list


def partition(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    ans = partition(data)[N//2]
    print(f'#{tc} {ans} {cnt}')