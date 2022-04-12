# SWEA 2115. 벌꿀채취

import sys
sys.stdin = open('input.txt')


def collect(r, c, worker, ans):
    global maxV

    profit = 0                              # 현재 위치에서 낼 수 있는 최대 이익
    for i in range(1 << M):
        honey = 0                           # C보다 적을만큼만 꿀 채취하도록 꿀의 양 담음
        total = 0                           # 해당 꿀에서 얻을 수 있는 수익
        for j in range(M):
            if i & (1 << j):
                honey += data[r][c+j]
                total += data[r][c+j] ** 2
        if honey <= C and profit < total:   # 만약 C이하로 꿀 채취하고 최대이익을 갱신할 수 있다면 갱신
            profit = total

    if worker >= 2:                         # 종료 조건(2명의 일꾼이 모두 꿀 채취)
        if ans + profit > maxV:             # 2번째 일꾼이 모은 이익까지 더한 값이 최대 이익보다 크다면 갱신
            maxV = ans + profit
        return

    if c + 2 * M - 1 < N:
        for cc in range(c+M, N-M+1):
            collect(r, cc, worker + 1, ans + profit)
    for rr in range(r+1, N):
        for cc in range(N-M+1):
            collect(rr, cc, worker + 1, ans + profit)


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # N: 벌통들의 크기, M: 선택할 수 있는 벌통의 개수, C: 꿀을 채취할 수 있는 최대 양
    data = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0                                # 최대 수익을 담을 변수
    for sr in range(N-1):
        for sc in range(N-M+1):
            collect(sr, sc, 1, 0)           # 첫 번째 일꾼이 고를 수 있는 벌통에서 꿀 채취
    print(f'#{tc} {maxV}')