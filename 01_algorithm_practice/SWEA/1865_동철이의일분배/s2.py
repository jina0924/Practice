# SWEA 1865. 동철이의 일 분배 - 통과

import sys
sys.stdin = open('input.txt')


def work(r):
    global p, ans
    if p < ans:                                 # 만약 뒤에 나올 확률이 계속 1이어도 최대값에 못미친다면
        return                                  # 이번 경우의 수 버림

    if r > N-1:                                 # 모든 직원에게 일을 맡겼다면
        if p > ans:                             # 모든 일의 성공 확률값 중 최대값 갱신
            ans = p
        return

    for c in range(N):                          # 해야 할 일 살펴보면서
        if not done[c] and data[r][c]:          # 아직 하지 않았고 해당 직원이 할 수 있는 일이라면
            p *= data[r][c] / 100               # 확률 곱해주고
            done[c] = 1                         # 일 성공했다고 체크
            work(r+1)                           # 다음 직원한테 일 맡기러 감
            done[c] = 0                         # 함수 반환된 후 현재값 초기화 해주고 해당 직원에게 다른일 시킴
            p /= data[r][c] / 100


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                            # N: 직원 수
    data = [list(map(int, input().split())) for _ in range(N)]  # data: 각 행의 직원이 일을 성공할 확률
    done = [0] * N                              # 일의 성공 여부 체크
    p, ans = 1, 0                               # p: 모든 일 성공 확률, ans: 그 확률 중 최댓값
    work(0)                                     # 0(1번쨰) 직원부터 일 배분
    print('#{} {:.6f}'.format(tc, ans * 100))   # 소수점 6번째까지 출력

