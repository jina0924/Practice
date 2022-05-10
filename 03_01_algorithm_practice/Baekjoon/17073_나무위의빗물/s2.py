# 백준 17073번 나무 위의 빗물

import sys
sys.stdin = open('input.txt')


N, W = map(int, sys.stdin.readline().split())        # N: 노드의 수, W: 1번 노드에 고인 물의 양
node = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    node[U] += 1
    node[V] += 1
leaf_cnt = 0
for i in range(2, N+1):
    if node[i] == 1:
        leaf_cnt += 1
print(W / leaf_cnt)