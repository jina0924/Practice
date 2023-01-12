# 백준 1764번 듣보잡

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
neverHeard, neverSeen = set(), set()
for _ in range(N):
    name = input()
    neverHeard.add(name)
for _ in range(M):
    name = input()
    neverSeen.add(name)
ans = sorted(list(neverHeard & neverSeen))
print(len(ans))
for p in ans:
    print(p.rstrip())