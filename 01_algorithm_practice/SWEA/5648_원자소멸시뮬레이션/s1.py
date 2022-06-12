# SWEA 5648. 원자 소멸 시뮬레이션 -5개

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())    # n: 원자들의 수
    matrix = [[0 for _ in range(2001)] for _ in range(2001)]    # 원자들의 위치를 표시할 행렬
    queue = deque([])
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        queue.append([x+1000, 1000-y, d, k])                    # 원자들을 동시에 출발시키기 위해 큐에 넣음
    delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    energy = 0
    while queue:
        v = queue.popleft()
        x, y, d, k = v[0], v[1], v[2], v[3]
        matrix[y][x] = k
        nx, ny = x + delta[d][0], y + delta[d][1]
        if 0 <= nx <= 2000 and 0 <= ny <= 2000:
            if not matrix[ny][nx]:
                matrix[ny][nx] = k
                matrix[y][x] = 0
                queue.append([nx, ny, d, k])
            else:
                energy += k

    print('#{} {}'.format(tc, energy))