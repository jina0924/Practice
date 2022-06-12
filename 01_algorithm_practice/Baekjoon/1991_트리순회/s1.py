# 백준 1991번 트리 순회

import sys
sys.stdin = open('input.txt')


def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree.get(node)[0])
        pre_order(tree.get(node)[1])
    return


def in_order(node):
    if node != '.':
        in_order(tree.get(node)[0])
        print(node, end='')
        in_order(tree.get(node)[1])
    return


def post_order(node):
    if node != '.':
        post_order(tree.get(node)[0])
        post_order(tree.get(node)[1])
        print(node, end='')
    return


N = int(input())
tree = {'A': [0, 0]}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = left, right

pre_order('A')
print()
in_order('A')
print()
post_order('A')