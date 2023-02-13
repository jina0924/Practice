# 백준 2475번 검증수

import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))
checksum = 0
for num in data:
    checksum += num ** 2
checksum %= 10
print(checksum)
