# 백준 14889번 스타트와 링크

import sys
sys.stdin = open('input3.txt')


def stat():
    A, B = 0, 0
    for i in range(N):
        for j in range(N):
            if team[i] and team[j]:
                A += data[i][j]
            elif team[i] == 0 and team[j] == 0:
                B += data[i][j]
    return abs(A - B)


def group(n, cnt):
    global ans
    if cnt == N // 2:
        result = stat()
        if result < ans:
            ans = result
    else:
        for i in range(n, N):
            if team[i] == 0:
                team[i] = 1
                group(i, cnt + 1)
                team[i] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
team = [0] * N
ans = 5000
for i in range(N//2):
    team[i] = 1
    group(i, 1)
    team[i] = 0
print(ans)