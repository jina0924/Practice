# 백준 1759번 암호 만들기

import sys
sys.stdin = open('input.txt')


def code(n):
    if n >= L:
        cnt = 0
        for char in result:
            if char in vowels:
                cnt += 1
        if 0 < cnt <= L - 2:
            print(''.join(result))
        return
    for i in range(C):
        if not data[i] in result and result[n-1] < data[i]:
            result[n] = data[i]
            code(n+1)
            result[n] = ''


L, C = map(int, input().split())    # L: 암호 길이, C: 주어지는 알파벳 개수
data = sorted(list(input().split()))
vowels = 'aeiou'
result = [''] * L
code(0)