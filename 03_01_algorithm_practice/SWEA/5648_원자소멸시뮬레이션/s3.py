# SWEA 5648. 원자 소멸 시뮬레이션 - 통과

import sys
sys.stdin = open('input.txt')


delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]                  # 상, 하, 좌, 우
def simulation():
    global energy

    while queue:
        x, y, d, k = queue.pop(0)
        if matrix[y][x] > k:                                # 만약 지금 위치에 저장된 에너지가 원자가 가진 에너지보다 크다면 = 충돌 상황
            energy += matrix[y][x]                          # 위치에 저장된 값 에너지에 더해줌
            matrix[y][x] = 0                                # 원자 소멸시킴
            continue                                        # 원자 소멸했으니까 새로운 위치 볼 것 없이 다음 원자 보러 감
        nx, ny = x + delta[d][0], y + delta[d][1]
        if 0 <= nx <= 4000 and 0 <= ny <= 4000:             # 새로운 위치가 범위 안에 있고
            if not matrix[ny][nx]:                          # 해당 위치가 비어있다면
                queue.append((nx, ny, d, k))                # 다음 번 위치를 살펴보기 위해 큐에 넣음
            matrix[ny][nx] += k                             # 0이든 값이 있든 우선 원자가 가진 에너지 더해줌
        matrix[y][x] = 0                                    # 새로운 위치 봤으면 현재 위치값 초기화해줌


T = int(input())

matrix = [[0 for _ in range(4001)] for _ in range(4001)]    # 원자들의 위치를 표시할 행렬
for tc in range(1, T+1):
    n = int(input())                                        # n: 원자들의 수
    queue = []                                              # 이동시킬 원자들을 담을 큐
    energy = 0                                              # 에너지 총합 변수(0으로 초기화
    for _ in range(n):
        x, y, d, k = map(int, input().split())              # x, y: 원자의 위치, d: 이동 방향, k: 보유 에너지
        if n > 1:                                           # n = 1일땐 충돌 없으므로 굳이 살펴볼 것 없음
            queue.append((2*x+2000, 2000-2*y, d, k))        # 원자들을 동시에 출발시키기 위해 큐에 넣음
    simulation()

    print('#{} {}'.format(tc, energy))