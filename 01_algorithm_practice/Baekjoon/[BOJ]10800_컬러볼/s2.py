# 백준 10800번 컬러볼 - 시간초과

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
balls = [[i] + list(map(int, input().split())) for i in range(N)]
balls.sort(key=lambda x: x[2])
print(balls)

# print(*ans, sep='\n')