"""
** 최소힙의 조건 **
1. 완전 이진 트리
2. 자식 < 부모 (왼쪽 & 오른쪽 자식의 크기는 상관 없음)
"""

def heap_push(value):
    global heap_count
    heap_count += 1                         # 원래 있던 heap 마지막 다음 자리에 push
    heap[heap_count] = value                # 넘겨받은 값을 해당 자리에 넣어줌
    child = heap_count                      # 현재 위치가 child
    parent = child // 2                     # 부모 위치값은 항상 child // 2

    while parent and heap[parent] > heap[child]:    # 부모가 자식보다 더 작을 때까지 위로 계속 거슬러 올라가기
        heap[parent], heap[child] = heap[child], heap[parent]   # 부모 값을 자식 값보다 더 작게 만들어줌
        child = parent                      # 현재 살펴본 부모가 자식일 때의 그 부모를 살펴봄
        parent = child // 2

def heap_pop():
    global heap_count
    return_value = heap[1]                  # heap에서 pop은 항상 루트에서 이루어짐
    heap[1] = heap[heap_count]              # 루트가 비어있으므로 heap의 마지막 값으로 채워넣어줌
    heap[heap_count] = 0                    # 비어있는 마지막 자리는 0으로 채워넣음
    heap_count -= 1

    parent = 1                              # 루트에서 시작
    child = parent * 2                      # 왼쪽 자식부터 살펴봄

    if child + 1 <= heap_count:             # 오른쪽 자식이 있다면
        if heap[child] > heap[child+1]:     # 왼쪽 자식이 오른쪽 자식보다 크다면
            child += 1                      # 부모와 비교할 자식은 오른쪽 자식이 됨(더 작은 값이랑 비교해서 최소힙 만들어야 되니까)

    # 자식이 있고, 그 자식이 부모보다 작다면 서로 교환해야함
    while child <= heap_count and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child                      # 자리 교환 후 해당 자식을 부모로 하는 서브트리 조사
        child = parent * 2                  # 그 부모의 왼쪽 자식 살펴봄

        if child + 1 <= heap_count:         # 오른쪽 자식 있다면 왼쪽 자식이랑 비교해서 더 작은 값 선택
            if heap[child] > heap[child + 1]:
                child += 1
    return return_value                     # 루트에서 pop한 값 반환


heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)             # 크기 설정 (+1은 인덱스를 노드 번호에 맞추기 위해서 설정)


#1. heap push
for i in range(N):
    heap_push(nums[i])         # 인덱스 0번에 해당하는 노드부터 heap_push 연산 수행
print(*heap)                   # 0 2 3 5 7 4 6

#2. heap pop
for i in range(N):             # 삭제 -> 루트 노드
    print(heap_pop(), end=' ') # 2 3 4 5 6 7