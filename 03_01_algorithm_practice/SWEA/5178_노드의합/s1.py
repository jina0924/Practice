# SWEA 5178. 노드의 합

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())     # n: 노드의 개수 / m: 리프 노드의 개수 / l: 노드 번호
    tree = [0 for _ in range(n+1)]          # 노드의 번호: 인덱스, 해당 인덱스의 값: 노드에 저장된 값
    for i in range(m):
        node, value = map(int, input().split())
        tree[node] = value
    while n > 1:                            # 루트에 도달할 때까지 반복 시행
        if not n % 2:                       # 만약 n이 짝수라면 -> 왼쪽자식만 남는 경우 발생
            tree[n//2] = tree[n]            # 왼쪽자식만 있으므로 부모와 왼쪽자식의 값이 같음
            n -= 1                          # 이 단계 전 노드로 넘어감
        else:                               # 만약 n이 홀수라면: 모든 부모가 자식 둘 씩 가짐
            tree[n//2] = tree[n-1] + tree[n]
            n -= 2                          # 이 전 부모, 자식 관계로 넘어감

    print(f'#{tc} {tree[l]}')