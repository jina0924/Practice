# SWEA 5202. 화물 도크

import sys
sys.stdin = open('input.txt')


def load(idx, end):                     # idx: 몇 번째 신청서인지, start: 현재 살펴보는 도크 작업 시작 시간, end: 끝나는 시간
    global cnt
    if end >= 24 or idx > N-1:          # 만약 모든 신청서를 살펴봤거나 이번에 살펴본 작업 완료 시간이 24라면
        return                          # 전체 작업 끝냄

    for i in range(idx, N):             # 현재 신청서부터 끝까지 살펴보면서
        if data[i][0] >= end:           # 만약 해당 작업 시작 시간이 현재 작업 끝나는 시간보다 뒤에 있다면
            cnt += 1                    # 이용 가능 화물차 1대 올려주고
            break                       # 더 뒤에 있는 신청서 살펴보지 않도록 break
    load(i, data[i][1])                 # 다음 작업시간 살피러 감


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                    # N: 도크 사용 신청서 개수
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1])       # 도크 작업 완료 시간을 기준으로 오름차순 정렬
    cnt = 1                             # 맨 앞 신청서부터 시작하므로 화물차 이용 가능 대수 1로 시작
    load(0, data[0][1])                 # 맨 앞 신청서 다음으로 가능한 신청서 살피러 감
    print(f'#{tc} {cnt}')