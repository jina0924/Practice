 # 백준 1937번 욕심쟁이 판다

import sys
sys.stdin = open('input.txt')

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def dfs():
    pass


n = int(input())
forest = []
bamboo = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        bamboo.append((data[c], r, c))
    forest.append(data)
bamboo.sort()
print(forest)
print(bamboo)