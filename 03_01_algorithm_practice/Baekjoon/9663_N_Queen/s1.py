# 백준 9663번 N-Queen
import sys
sys.stdin = open('input.txt')


def queen(r):
    global cnt
    if r >= N:
        cnt += 1
        return
    for c in range(N):
        if not used_r[r] and not used_c[c] and not used_d1[r+c] and not used_d2[r-c]:
            used_r[r] = used_c[c] = used_d1[r+c] = used_d2[r-c] = 1
            queen(r+1)
            used_r[r] = used_c[c] = used_d1[r+c] = used_d2[r-c] = 0


N = int(input())
cnt = 0
used_r = [0] * N
used_c = [0] * N
used_d1 = [0] * (2 * N - 1)     # 우상향 대각선
used_d2 = [0] * (2 * N - 1)     # 우하향 대각선
queen(0)
print(cnt)