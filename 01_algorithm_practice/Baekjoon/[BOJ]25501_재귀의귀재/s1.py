# 백준 25501번 재귀의 귀재

import sys
sys.stdin = open('input.txt')


def recursion(word, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif word[l] != word[r]:
        return 0, cnt
    else:
        return recursion(word, l+1, r-1, cnt+1)


def isPalindrome(word):
    return recursion(word, 0, len(word) - 1, 1)


T = int(input())
for tc in range(T):
    S = input()
    print(*isPalindrome(S))