# 백준 1043번 거짓말

import sys
sys.stdin = open('input8.txt')
input = sys.stdin.readline


N, M = map(int, input().split())        # N: 사람의 수, M: 파티의 수
already = set(input().split()[1:])      # set으로 진실을 아는 사람들 저장해둠

parties = [set(input().split()[1:]) for _ in range(M)]      # 각 파티에 오는 사람들 정보

'''
M번 반복하는 이유: 
맨 마지막에 already에 추가된다면 모든 파티를 다시 돌면서 사람들을 확인해야 함
'''
for _ in range(M):
    for party in parties:
        if party & already:
            already = already | party

ans = 0
for i in range(M):
    if not set(parties[i]) & already:
        ans += 1
print(ans)