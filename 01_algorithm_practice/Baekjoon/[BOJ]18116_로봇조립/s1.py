# 백준 18116번 로봇 조립 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# python에서 재귀 횟수 제한있음(10 ** 3) => 제한을 늘려주는 장치


def find_set(x):
    # while p[x] != x:
    #     x = p[x]
    # return x
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px, py = find_set(x), find_set(y)
    if px < py:
        p[py] = px
        s[px] += s[py]
        s[py] = 0
    else:
        p[px] = py
        s[py] += s[px]
        s[px] = 0


N = int(input())
p = [i for i in range(1000001)]
s = [1] * 1000001
for _ in range(N):
    direc = input().split()
    if direc[0] == 'I':
        a, b = int(direc[1]), int(direc[2])
        if find_set(a) != find_set(b):          # 부모 노드가 같은 경우에도 union하면 s[a]에 불필요한 값 누적하게 됨
            union(a, b)
    else:
        tmp = find_set(int(direc[1]))
        # print(p.count(tmp))   count 시간 오래걸림
        print(s[tmp])