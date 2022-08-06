# 백준 1043번 거짓말

import sys
sys.stdin = open('input8.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
already = set(input().split()[1:])
parties = []

# for _ in range(M):
#     parties.append(set(input().split()[1:]))

for num in range(M):
    party = set(input().split()[1:])
    if party & already:
        already = already | party
    parties.append(party)
    # for j in range(num+1):
    i = 0
    while i < num+1:
        if parties[i] & already:
            already = already | parties[i]
            i = 0
        else:
            i += 1
ans = 0
for i in range(M):
    if not set(parties[i]) & already:
        ans += 1
print(ans)