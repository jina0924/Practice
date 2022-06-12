# SWEA 5648. 원자 소멸 시뮬레이션 - 40개

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 상, 하, 좌, 우
matrix = [[0 for _ in range(4001)] for _ in range(4001)]  # 원자들의 위치를 표시할 행렬
for tc in range(1, T+1):
    n = int(input())    # n: 원자들의 수
    queue = deque([])
    for _ in range(n):
        x, y, d, k = map(int, input().split())              # x, y: 원자의 위치, d: 이동 방향, k: 보유 에너지
        queue.append((2*x+2000, 2000-2*y, d, k))            # 원자들을 동시에 출발시키기 위해 큐에 넣음
    energy = 0
    while queue:
        v = queue.popleft()
        x, y, d, k = v[0], v[1], v[2], v[3]
        if not matrix[y][x] or matrix[y][x] == k:
            matrix[y][x] = k
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx <= 4000 and 0 <= ny <= 4000:
                if not matrix[ny][nx]:
                    matrix[ny][nx] = k
                    queue.append((nx, ny, d, k))
                else:
                    matrix[ny][nx] += k
                matrix[y][x] = 0
            else:
                matrix[y][x] = 0
        elif matrix[y][x] != k:
            energy += matrix[y][x]
            matrix[y][x] = 0
            continue

    print('#{} {}'.format(tc, energy))