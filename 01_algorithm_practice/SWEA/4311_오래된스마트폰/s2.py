# SWEA 4311. 오래된 스마트폰 - 라이브러리 사용 금지

import sys
sys.stdin = open('input.txt')
import heapq


def touch():
    num2 = []
    num3 = []
    for i in range(N):
        for j in range(N):
            if num1[i] * 10 + num1[j] == W:
                return 2
            elif 0 <= num1[i] * 10 + num1[j] < 1000 and num1[i]:
                num2.append(num1[i] * 10 + num1[j])
    for i in range(len(num2)):
        for j in range(N):
            if num2[i] * 10 + num1[j] == W:
                return 3
            elif 0 <= num2[i] * 10 + num1[j] < 1000:
                num3.append(num2[i] * 10 + num1[j])

    heap = []
    for num in num1:
        heapq.heappush(heap, (1, num))
    for num in num2:
        heapq.heappush(heap, (2, num))
    for num in num3:
        heapq.heappush(heap, (3, num))

    while heap:
        cnt, num = heapq.heappop(heap)
        for o in range(O):
            for i in range(len(num1)):
                if opers[o] == 1:
                    nnum = num + num1[i]
                elif opers[o] == 2:
                    nnum = num - num1[i]
                elif opers[o] == 3:
                    nnum = num * num1[i]
                elif opers[o] == 4:
                    if num1[i] == 0:
                        continue
                    else:
                        nnum = num // num1[i]
                if cnt + 2 <= M and 0 <= nnum <= 999:
                    if nnum == W and cnt + 3 <= M:
                        return cnt + 3
                    else:
                        heapq.heappush(heap, (cnt + 2, nnum))
            for i in range(len(num2)):
                if opers[o] == 1:
                    nnum = num + num2[i]
                elif opers[o] == 2:
                    nnum = num - num2[i]
                elif opers[o] == 3:
                    nnum = num * num2[i]
                elif opers[o] == 4:
                    nnum = num // num2[i]
                if cnt + 3 <= M and 0 <= nnum <= 999:
                    if nnum == W and cnt + 4 <= M:
                        return cnt + 4
                    else:
                        heapq.heappush(heap, (cnt + 3, nnum))
            for i in range(len(num3)):
                if opers[o] == 1:
                    nnum = num + num3[i]
                elif opers[o] == 2:
                    nnum = num - num3[i]
                elif opers[o] == 3:
                    nnum = num * num3[i]
                elif opers[o] == 4:
                    nnum = num // num3[i]
                if cnt + 4 <= M and 0 <= nnum <= 999:
                    if nnum == W and cnt + 5 <= M:
                        return cnt + 5
                    else:
                        heapq.heappush(heap, (cnt + 4, nnum))

    return -1


T = int(input())

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    num1 = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    W = int(input())
    print(f'#{tc} {touch()}')
