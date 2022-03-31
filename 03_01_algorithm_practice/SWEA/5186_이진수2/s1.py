# SWEA 5186. 이진수2

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())              # N: 소수점 아래 12자리 이내인 양수
    ans = ''                        # 0.을 제외한 나머지 숫자를 담을 변수
    pos = 1                         # 소수점 자리를 체크할 변수
    while N > 0:
        if (0.5) ** pos <= N:       # N이 해당 자리수가 1일 때의 값보다 크다면
            ans += '1'              # 소수점 자리에 1 추가함
            N -= (0.5) ** pos       # N을 자리수만큼 빼줌
        else:                       # 해당 자리수보다 N이 작다면 뺄 수 없으므로
            ans += '0'              # 소수점 자리에 0 추가함
        pos += 1                    # 자리수 1 늘려줌
        if pos == 14:               # 13이 아닌 이유: 매 반복 끝에 1을 더해주므로 12자리까지 와도 overflow가 올 수 있음
            ans = 'overflow'
            break
    print(f'#{tc} {ans}')