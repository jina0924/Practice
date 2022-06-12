# SWEA 1242. 암호코드 스캔

import sys
sys.stdin = open("input.txt")
from collections import deque

# 16진수 -> 2진수
asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

# 암호비트패턴
code = {
    0: (2, 1, 1),
    1: (2, 2, 1),
    2: (1, 2, 2),
    3: (4, 1, 1),
    4: (1, 3, 2),
    5: (2, 3, 1),
    6: (1, 1, 4),
    7: (3, 1, 2),
    8: (2, 1, 3),
    9: (1, 1, 2),
}

# ASCII -> Hexadecimal
def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10

def hex_to_binary(x):
    for i in range(4):
        t.append(asc[x][i])

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pwd = [input().rstrip('0') for _ in range(N)]
    for row in pwd:                     # 가로로 한 줄씩 살펴보면서 고유번호가 있는지 판별
        if row == '':                   # 가로의 모든 번호가 0이라면 암호 없으므로 다음 가로줄 살펴봄
            continue

        t = []
        serial = deque([])              # 상품 고유 번호를 담을 리스트
        pos = -1                        # 상품 번호가 있는 부분 찾을 인덱스

        for i in range(len(row)):
            hex_to_binary(ascii_to_hex(row[i]))
        print(''.join(map(str, t)))