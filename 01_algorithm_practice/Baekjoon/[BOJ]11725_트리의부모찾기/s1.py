# 백준 11725번 트리의 부모 찾기

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
from collections import defaultdict


def find_p(x):
    queue = [x]

    while queue:
        x = queue.pop(0)
        for next in tree[x]:
            if not p[next]:
                queue.append(next)
                p[next] = x


N = int(input())                            # N: 노드의 개수
tree = defaultdict(list)                    # 리스트를 딕셔너리 초기값으로 설정 -> value에 연결 노드 담을 예정
p = [0] * (N + 1)                           # 노드의 부모를 저장할 배열
p[1] = 1                                    # 트리의 루트 = 1
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
find_p(1)
print(*p[2:], sep='\n')