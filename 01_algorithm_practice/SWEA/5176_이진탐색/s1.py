# SWEA 5176. 이진 탐색

import sys
sys.stdin = open('input.txt')

def in_order(node):                             # 중위순회의 순서대로 노드에 값 넣음
    global num                                  # 방문 순서대로 넣을 값의 변수
    if node:                                    # 만약 노드가 0이 아니라면 = 값이 있다면
        in_order(tree[node][0])                 # 왼쪽 자식 먼저 살펴봄
        tree[node][1] = num                     # 현재 위치에 값 넣고
        num += 1                                # 다음에 넣을 값을 위해 1 더해줌
        in_order(tree[node][2])                 # 오른쪽 자식 살펴봄
    return

T = int(input())

for tc in range(1, T + 1):
    n = int(input())                            # n: 노드 개수
    tree = [[0, 0, 0] for i in range(n+1)]      # 인덱스 0: 왼쪽 자식, 인덱스 1: 본인, 인덱스 2: 오른쪽 자식
    for i in range(1, n+1):
        if i*2+1 <= n:                          # 만약 오른쪽 자식이 있다면
            tree[i][0], tree[i][2] = i*2, i*2+1 # 왼쪽 자식도 있으므로 둘 다 인덱스값 넣어줌
        elif i*2 <= n:                          # 왼쪽 자식만 있다면
            tree[i][0] = i*2                    # 왼쪽 자식의 인덱스 지정해줌
    num = 1
    in_order(1)

    print('#{} {} {}'.format(tc, tree[1][1], tree[n//2][1]))