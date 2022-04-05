# SWEA 5209. 최소 생산 비용

import sys
sys.stdin = open('input.txt')


def product(r):
    global cost, ans
    if cost >= ans:                     # 만약 현재까지 비용이 ans값보다 크다면
        return                          # 더 볼 필요 없으므로 return

    if r > N-1:                         # 마지막 제품까지 생산했고
        if cost < ans:                  # 총 비용이 전에 있던 최소 비용보다 적다면 갱신
            ans = cost
        return

    for c in range(N):                  # 제품별로 확인하면서
        if not made[c]:                 # 아직 만들지 않은 제품이라면
            made[c] = 1                 # 만들었단 표시 해주고
            cost += factory[r][c]       # 해당 비용 추가해줌
            product(r+1)                # 다음 제품 만들러 감
            made[c] = 0                 # 함수 반환되면 해당 제품 생산 여부 초기화해주고 다른 공장 비용 살펴봄
            cost -= factory[r][c]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                    # N: 제품 수
    factory = [list(map(int, input().split())) for _ in range(N)]   # 공장별 생산 비용
    cost, ans = 0, 22500                # cost: 매번 발생하는 비용, ans: 최종적으로 최소 비용을 담을 변수
    made = [0] * N                      # 제품 생산 여부 표시할 배열
    product(0)
    print(f'#{tc} {ans}')