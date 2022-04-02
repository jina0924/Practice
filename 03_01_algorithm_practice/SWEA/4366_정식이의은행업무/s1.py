# SWEA 4366. 정식이의 은행업무

import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    binary = list(map(int, input()))        # 2진수 입력
    ternary = list(map(int, input()))       # 3진수 입력
    tset = set()                            # 3진수 후보를 담을 set
    ternary.reverse()                       # 인덱스값을 지수로 올리기 위해 반대로 뒤집음
    num = 0
    for i in range(len(ternary)):           # 현재 3진수 값으로 10진수 초기값 설정
        num += ternary[i] * 3 ** i
    for k in range(len(ternary)):           # 틀릴 수 있는 위치별로 반복
        if ternary[k] == 2:                 # 살펴본 위치의 수가 2라면 1 또는 0이 옳은 값(이하 생략)
            tset.add(num - 3 ** k)
            tset.add(num - 2 * 3 ** k)
        elif ternary[k] == 1:
            tset.add(num - 3 ** k)
            tset.add(num + 3 ** k)
        elif ternary[k] == 0:
            tset.add(num + 3 ** k)
            tset.add(num + 2 * 3 ** k)
    binary.reverse()
    for k in range(len(binary)-1):          # 틀릴 수 있는 위치 인덱스를 k로 잡음
        bnum = 0                            # 10진수를 담을 변수 초기화
        for i in range(len(binary)):        # 2진수 전체를 돌면서
            if k == i:                      # 현재 위치가 틀릴 것으로 추정된 위치라면
                if binary[k]:               # 0이면 1로, 1이면 0으로 바꿔서 더해줌
                    continue
                else:
                    bnum += 1 * 2 ** i
            else:
                bnum += binary[i] * 2 ** i
        if bnum in tset:                    # 지금 살펴본 2진수가 3진수에서 살펴본 수라면
            ans = bnum                      # 최종값으로 현재 수를 담고
            break                           # 반복 끝냄

    print('#{} {}'.format(tc, ans))

