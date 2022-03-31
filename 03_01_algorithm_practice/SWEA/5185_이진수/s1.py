# SWEA 5185. 이진수

import sys
sys.stdin = open('input.txt')

asc = {
    0: '0000',
    1: '0001',
    2: '0010',
    3: '0011',
    4: '0100',
    5: '0101',
    6: '0110',
    7: '0111',
    8: '1000',
    9: '1001',
    10: '1010',
    11: '1011',
    12: '1100',
    13: '1101',
    14: '1110',
    15: '1111'
}

T = int(input())

for tc in range(1, T+1):
    N, ascii_num = input().split()      # N: 자리 수, ascii_num: 16진수
    ans = ''
    for c in ascii_num:                 # 16진수의 각 자리 수별로 살펴보기
        if c <= '9':                    # 0 ~ 9일 때
            hex_num = ord(c) - ord('0')
        else:                           # A(10) ~ F(15)일 때
            hex_num = ord(c) - ord('A') + 10
        ans += asc.get(hex_num)         # 해당 숫자의 이진수 더해줌

    print(f'#{tc} {ans}')