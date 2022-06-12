# SWEA 5177. 이진힙

import sys
sys.stdin = open('input.txt')

def heap_push(idx, node):                       # 힙 삽입 함수
    heap[idx] = node                            # 해당 인덱스에 노드 값 넣어줌
    child = idx                                 # 현재 인덱스 = 자식
    parent = child // 2                         # 현재 인덱스의 부모 인덱스값 설정

    while parent and heap[parent] >= heap[child]:   # 만약 부모가 있고, 그 부모의 값이 자식값보다 크다면
        heap[parent], heap[child] = heap[child], heap[parent]   # 값 서로 바꿔주고
        child = parent                          # 그 부모를 자식으로 하는 트리 구조 살펴보기
        parent = child // 2

T = int(input())

for tc in range(1, T + 1):
    n = int(input())                            # n: 노드의 개수
    data = list(map(int, input().split()))
    heap = [0] * (n+1)                          # 인덱스로 접근하기 위해 노드의 개수보다 1 큰 heap 만듦
    for idx, node in enumerate(data):           # 각 인덱스에 해당하는 노드 값 저장하기 위해 enumerate로 순환
        heap_push(idx+1, node)
    total = 0                                   # 조상 노드의 합을 담을 변수
    while n > 1:                                # 루트가 1이므로 루트까지 가도록 반복
        n //= 2                                 # 마지막 노드의 조상으로 거슬러 올라감
        total += heap[n]

    print('#{} {}'.format(tc, total))