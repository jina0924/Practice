# 백준 4889번 안정적인 문자열

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = 1
while True:
    data = input().rstrip()
    if data[0] == '-':
        sys.exit()
    cnt = 0
    isOpen = False
    for i in range(len(data) // 2):
        left, right = data[i], data[-i - 1]
        if left == right:
            cnt += 1
        else:
            if left == '}':
                if not isOpen:
                    cnt += 2
                    isOpen = True
                else:
                    isOpen = False
            else:
                if isOpen:
                    cnt += 2
                    isOpen = False
                else:
                    isOpen = True


    print(f'{tc}. {cnt}')
    tc += 1