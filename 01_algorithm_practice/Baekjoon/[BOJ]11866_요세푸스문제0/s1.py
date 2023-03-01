# 백준 11866번 요세푸스 문제 0

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())        # N, K: 원을 이룰 원소 수, K번째 제거
nums = [i for i in range(1, N + 1)]
ans = []
out = K - 1                             # nums에서 제거할 인덱스 변수
while N:                                # nums에 원소가 남아있을때까지 반복
    if nums[out]:
        ans.append(nums[out])
        nums.pop(out)
        N = len(nums)
        if N == 0:
            print('<', end='')
            print(*ans, sep=', ', end='')
            print('>')
            sys.exit()
        out = (out + K-1) % N
    else:
        N = len(nums)
        out = (out + 1) % N