# 백준 14267번 회사 문화1 - 통과

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())            # n, m : 회사 직원 수, 최초의 칭찬 횟수
data = list(map(int, input().split()))      # 직속 상사의 번호
tree = defaultdict(list)
for i in range(1, n):
    tree[data[i]].append(i + 1)
ans = [0] * (n + 1)                         # 각자 받은 칭찬 수치 저장할 배열(인덱싱 편하게 하기 위해 (n+1)만큼 마련
praise = [0] * (n + 1)                      # 최초로 받은 칭찬 저장할 배열
for _ in range(m):
    i, w = map(int, input().split())        # i, w : 칭찬을 받은 직원 번호, 칭찬의 수치
    praise[i] += w
for j in range(1, n + 1):
    ans[j] += praise[j]                     # 직속 상사에게 받은 칭찬 저장
    for c in tree[j]:                       # 직속 부하에게 칭찬 부여
        ans[c] += ans[j]
print(*ans[1:])                             # 1번 ~ n번 직원 결과값 출력