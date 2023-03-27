# 백준 4889번 안정적인 문자열

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = 1
while True:
    data = input().rstrip()
    if data[0] == '-':
        sys.exit()
    stack = []
    cnt = 0
    for i in range(len(data)):
        if data[i] == '{':
            stack.append(data[i])
        else:
            if stack:
                stack.pop()
            else:
                stack.append('{')
                cnt += 1
    if stack:
        cnt += len(stack) // 2
    print(f'{tc}. {cnt}')
    tc += 1