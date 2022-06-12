# SWEA 2819. 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open('input.txt')

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]              # 동, 서, 남, 북
def make_num(r, c, n, num):
    if n == 7:                                          # 총 7자리 수가 만들어지면
        num_set.add(num)                                # num_set에 해당 수를 넣어주고
        return                                          # 함수를 종료시킴
    for d in range(4):                                  # 동, 서, 남, 북 방향으로 살펴보면서
        nr, nc = r + delta[d][0], c + delta[d][1]
        if 0 <= nr < 4 and 0 <= nc < 4:                 # 해당 위치가 격자판 안에 있다면
            make_num(nr, nc, n+1, num + grid[nr][nc])   # 숫자 이어주고 다음 위치 살피러 감

T = int(input())

for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]    # 입력받은 격자판
    num_set = set()                                     # 중복 제거하기 위해 set으로 숫자 받음
    for r in range(4):
        for c in range(4):
            make_num(r, c, 1, grid[r][c])               # 임의의 위치에서 시작

    print('#{} {}'.format(tc, len(num_set)))
