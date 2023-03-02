# 백준 1259번 팰린드롬수

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline              # 윗줄 코드와 순서 바꾸면 제대로 동작x

while True:
    num = input().rstrip()
    if num == '0':
        sys.exit()
    if num == num[::-1]:
        print('yes')
    else:
        print('no')