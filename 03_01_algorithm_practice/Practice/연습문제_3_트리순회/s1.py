# 연습 문제3. 트리 순회


def pre_order(node):
    if node:
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][2])

# 중위 순회 (L -> V -> R)
def in_order(node):
    if node:
        in_order(tree[node][0])
        print(node, end=' ')
        in_order(tree[node][2])

# 후위 순회 (L -> R -> V)
def post_order(node):
    if node:
        post_order(tree[node][0])
        post_order(tree[node][2])
        print(node, end=' ')


import sys
sys.stdin = open('input.txt')

V = int(input())
data = list(map(int, input().split()))
tree = [[0, 0, 0] for _ in range(V+1)]
for i in range(V-1):
    p, c = data[i*2], data[i*2+1]
    if tree[p][0]:
        tree[p][2] = c
    else:
        tree[p][0] = c
    tree[c][1] = p

print(tree)

print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()