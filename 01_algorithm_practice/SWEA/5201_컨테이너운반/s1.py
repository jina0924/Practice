# SWEA 5201. 컨테이너 운반

import sys
sys.stdin = open('input.txt')

def load(t, f, w):
    global ans
    if t > M - 1 or f > N - 1:                  # 만약 모든 트럭을 살펴봤거나 컨테이너를 모두 살펴봤다면
        if ans < w:                             # 현재 총 중량이 기존 값보다 크다면 갱신해줌
            ans = w
        return

    if truck[t] >= freight[f]:                  # 만약 현재 살펴보는 트럭의 적재 용량이 컨테이너 무게보다 크다면
        load(t+1, f+1, w + freight[f])          # 해당 컨테이너를 싣고 다음 트럭과 컨테이너 살펴봄
    else:                                       # 현재 트럭으로 해당 컨테이너를 못 싣는다면 => 다음 트럭도 못 담음
        load(t, f+1, w)                         # 그보다 작은 컨테이너 무게 살피러 감

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())            # N: 컨테이너 수, M: 트럭 수
    freight = list(map(int, input().split()))   # N개의 화물의 무게
    freight.sort(reverse=True)                  # 내림차순으로 정렬해줌
    truck = list(map(int, input().split()))     # M개 트럭의 적재 용량
    truck.sort(reverse=True)                    # 내림차순 정렬
    ans = 0                                     # 최대 화물 총 중량의 초기값 0으로 설정(한 개도 옮길 수 없는 경우)
    load(0, 0, 0)                               # 제일 무거운 컨테이너, 적재 용량 가장 큰 트럭부터 적재하러 감
    print(f'#{tc} {ans}')