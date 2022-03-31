# SWEA 1240. 단순 2진 암호코드

import sys
sys.stdin = open("input.txt")
from collections import deque

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pwd = [list(map(int, input())) for _ in range(N)]
    for row in pwd:                     # 가로로 한 줄씩 살펴보면서 고유번호가 있는지 판별
        serial = deque([])              # 상품 고유 번호를 담을 리스트
        pos = -1                        # 상품 번호가 있는 부분 찾을 인덱스

        if not sum(row):                # 가로의 모든 번호가 0이라면 암호 없으므로 다음 가로줄 살펴봄
            continue

        # 뒤에서 1 찾기
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 1:             # 암호의 끝부분을 찾았다면
                pos = i                 # 끝부분 인덱스 저장해주고
                break                   # 해당 암호 인덱스 찾기 끝냄
        break                           # 암호부분 찾았으므로 전체 암호 코드 더 이상 살펴보지 않아도 됨

    while len(serial) < 8:              # 8개의 숫자를 발견할 때까지 반복
        x = code[row[pos - 6]][row[pos - 5]][row[pos - 4]][row[pos - 3]][row[pos - 2]][row[pos - 1]][row[pos]]
        serial.appendleft(x)
        pos -= 7

    ans = 0
    for i in range(4):
        ans += serial[i*2] * 3 + serial[i*2+1]  # 홀수 자리 수는 3배, 짝수 자리 수는 그냥 더함

    if ans % 10:                        # 만약 고유 번호의 계산 값이 10의 배수가 아니라면
        ans = 0                         # 비정상적인 암호코드이므로 0 출력
    else:
        ans = sum(serial)               # 정상적인 코드라면 숫자들의 합 출력

    print(f'#{tc} {ans}')