"""
연습 문제1.
"""

# 병합 정렬
def merge(left, right):
    sorted_list = [0] * (len(left) + len(right))    # 정렬된 수 담을 리스트

    l = r = i = 0                                   # l: left의 인덱스, r: right의 인덱스, i: sorted_list의 인덱스
    while l < len(left) and r < len(right):         # left와 right 둘 중 하나라도 다 털어버릴때까지
        if left[l] < right[r]:                      # 왼쪽의 값이 오른쪽 값보다 작다면
            sorted_list[i] = left[l]                # sorted_list에 넣어주고
            l += 1                                  # l 인덱스를 한 칸 옮김
        else:                                       # 오른쪽도 마찬가지
            sorted_list[i] = right[r]
            r += 1
        i += 1                                      # 왼쪽이든 오른쪽이든 담았다면 i 인덱스 한 칸 옮김

    while l < len(left):                            # left의 값을 털어버릴 때까지 sorted_list에 담기
        sorted_list[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        sorted_list[i] = right[r]
        r += 1
        i += 1

    return sorted_list

def partition(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left, right)


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


# 퀵 정렬
def quick_sort(arr, start, end):
    if start < end:                             # start와 end가 같지 않다 = 아직 정렬할게 남았다
        pivot = partition(arr, start, end)      # pivot = 기준값
        quick_sort(arr, start, pivot-1)         # pivot보다 작은 값들 정렬
        quick_sort(arr, pivot+1, end)           # pivot보다 큰 값들 정렬
    return arr


def partition(arr, start, end):
    pivot = arr[start]                          # 피봇 = 넘겨받은 배열의 첫 번째 요소
    left = start + 1                            # left: 피봇 바로 다음 값
    right = end                                 # right: 제일 끝 값
    done = False                                # 피봇이 위치할 자리 잡았는지 표시할 변수
    while not done:                             # 피봇 자리 잡을 때까지 반복
        while left <= right and arr[left] <= pivot:     # 피봇보다 큰 값 찾을 떄까지 반복
            left += 1
        while left <= right and pivot <= arr[right]:    # 피봇보다 작은 값 찾을 떄까지 반복
            right -= 1
        if right < left:                        # right와 left가 교차하면 교차점이 피봇 자리
            done = True
        else:                                   # 교차하지 않았다면
            arr[left], arr[right] = arr[right], arr[left]   # 피봇보다 작은 값과 큰 값 자리를 맞추기 위해 서로 자리바꿈
    arr[start], arr[right] = arr[right], arr[start]     # 피복 자리 찾았으면 right값과 자리바꿈
    return right                                # right가 새로운 피봇 인덱스


quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)
print(quick_sort(numbers, 0, len(numbers) - 1))