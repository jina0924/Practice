# 백준 3967번 매직 스타

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# print(ord("A"), ord("Z"))
star = []
known = []
for r in range(5):
    row = list(input().rstrip())
    for c in range(9):
        if row[c] == '.':
            row[c] = 0
        elif row[c] == 'x':
            row[c] = -1
        else:
            row[c] = ord(row[c]) - 64
            known.append((r, c))
    star.append(row)
print(star)

