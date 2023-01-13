# 백준 1764번 듣보잡

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
neverHeard, ans = set(), set()
for _ in range(N):
    name = input()
    neverHeard.add(name)
for _ in range(M):
    name = input()
    if name in neverHeard:
        ans.add(name)
ans = sorted(list(ans))
l = len(ans)
print(l)
for p in ans:
    print(p.rstrip())