# 백준 1991번 트리 순회

import sys
sys.stdin = open('input.txt')
from collections import defaultdict


def preorder(v):
    if v.isalpha():                 # 자식 노드가 없을 경우 '.'으로 입력되므로 자식 노드가 알파벳으로 있는지 확인
        print(v, end='')
    for c in tree[v]:
        preorder(c)


def inorder(v):
    if tree[v][0].isalpha():
        inorder(tree[v][0])
    print(v, end='')
    if tree[v][1].isalpha():
        inorder(tree[v][1])


def postorder(v):
    for c in tree[v]:
        postorder(c)
    if v.isalpha():
        print(v, end='')


N = int(input())
tree = defaultdict(list)
for _ in range(N):
    p, l, r = input().split()
    tree[p] = [l, r]
preorder('A')                   # 전위 순회
print()
inorder('A')                    # 중위 순회
print()
postorder('A')                  # 후위 순회
