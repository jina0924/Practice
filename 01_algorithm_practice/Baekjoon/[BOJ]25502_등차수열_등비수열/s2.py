# 백준 25502번 등차수열? 등비수열? - 50% x

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(M):
    i, x = map(int, input().split())
    A[i-1] = x
    ans = '+'
    if 1 < i < N:
        a, b = A[i] - A[i-1], A[i-1] - A[i-2]
        if a <= 0 or a != b:
            ans = '*'
            c, d = A[i] / A[i-1], A[i-1] / A[i-2]
            if c <= 0 or c != int(c) or c != d:
                ans = '?'
    elif i == 1:
        a, b = A[2] - A[1], A[1] - A[0]
        if a <= 0 or a != b:
            ans = '*'
            c, d = A[2] / A[1], A[1] / A[0]
            if c <= 0 or c != int(c) or c != d:
                ans = '?'
    elif i == N:
        a, b = A[i-1] - A[i-2], A[i-2] - A[i-3]
        if a <= 0 or a != b:
            ans = '*'
            c, d = A[i-1] / A[i-2], A[i-2] / A[i-3]
            if c <= 0 or c != int(c) or c != d:
                ans = '?'
    print(ans)

    # d, r = A[1] - A[0], A[1] / A[0]
    # ans = '+'
    # if d <= 0:
    #     ans = '*'
    #     if r <= 0:
    #         ans = '?'
    #         continue
    # for i in range(2, N):
    #     if A[i] - A[i-1] != d:
    #         ans = '*'
    #         if A[i] / A[i-1] != r:
    #             ans = '?'
    #             break
    # print(ans)