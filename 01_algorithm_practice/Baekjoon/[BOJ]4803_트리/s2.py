# 백준 4803번 트리 - 시간초과 -> pypy3 통과

import sys
sys.stdin = open('input.txt')


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


tc = 0
while True:
    v, e = map(int, input().split())
    cycle = {0}
    p = [i for i in range(v+1)]
    if v == 0:
        break
    for _ in range(e):
        a, b = map(int, input().split())
        A = find_set(a)
        B = find_set(b)
        if A == B:
            cycle.add(A)
        else:
            union(a, b)
    for i in range(1, v+1):
        p[i] = find_set(i)
        # if i in cycle:
        #     cycle.add(p[i])
    tc += 1
    T = len(set(p) - cycle)
    if not T:
        print(f'Case {tc}: No trees.')
    elif T == 1:
        print(f'Case {tc}: There is one tree.')
    elif T > 1:
        print(f'Case {tc}: A forest of {T} trees.')