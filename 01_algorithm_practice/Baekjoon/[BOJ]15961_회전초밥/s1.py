# 백준 15961번 회전초밥 - x

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N, d, k, c = map(int, input().split())          # 초밥 벨트에 놓인 접시 수, 초밥 가짓수, 연속으로 먹는 수, 쿠폰 번호
sushi_cnt = [0] * (d + 1)                       # 먹는 구간의 초밥 개수 셀 배열
sushi_cnt[c] += 1                               # 쿠폰으로 받은 초밥 무조건 먹으니까 +1
belt = [int(input()) for _ in range(N)]
start, end = 0, k-1                             # 먹는 구간의 시작과 끝
total = k + 1                                   # 현재 구간에서 먹을 수 있는 초밥 종류의 개수를 담을 변수
for i in range(k):
    sushi_cnt[belt[i]] += 1
    if sushi_cnt[belt[i]] >= 2:                 # 중복된 종류면
        total -= 1                              # 개수 -1
ans = total
while start < N:                                # 벨트 한바퀴 돌 때까지 반복
    sushi_cnt[belt[start]] -= 1                 # 전 구간에서 본 맨 앞 초밥 개수 조정
    if sushi_cnt[belt[start]] == 0:             # 이전에 유일한 종류였다면
        total -= 1                              # 초밥 종류 -1
    start += 1                                  # 구간 변경
    if end < N - 1:
        end += 1
    else:                                       # 회전 구조니까 맨 끝을 넘어가면 처음으로 맞추기
        end = 0
    sushi_cnt[belt[end]] += 1
    if sushi_cnt[belt[end]] < 2:                # 추가된 초밥 종류가 이전에 못 본거면
        total += 1                              # 초밥 종류 +1
    ans = max(ans, total)                       # 최대값 갱신
print(ans)