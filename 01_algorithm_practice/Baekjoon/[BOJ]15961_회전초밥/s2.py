# 백준 15961번 회전초밥

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline
from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
sushi = defaultdict(int)
start, end = 0, k
