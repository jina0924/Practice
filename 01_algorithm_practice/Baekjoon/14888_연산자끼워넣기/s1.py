# 백준 14888번 연산자 끼워넣기

import sys
sys.stdin = open('input3.txt')


def calc(idx, res):
    if idx >= N:
        results.add(res)
        return
    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            if i == 0:
                calc(idx+1, res + nums[idx])
            elif i == 1:
                calc(idx+1, res - nums[idx])
            elif i == 2:
                calc(idx+1, res * nums[idx])
            elif i == 3:
                if res >= 0:
                    calc(idx+1, res // nums[idx])
                else:
                    calc(idx+1, -(-res // nums[idx]))
            ops[i] += 1


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
results = set()
calc(1, nums[0])
print(max(results))
print(min(results))
