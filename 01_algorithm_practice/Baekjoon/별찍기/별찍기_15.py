# 백준 10990번 별 찍기-15

N = int(input())
for i in range(N):
    for j in range(N + i):
        if j == N - 1 - i or j == N - 1 + i:
            print('*', end='')
        else:
            print(' ', end='')
    print()