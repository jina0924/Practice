# 백준 11559번 Puyo Puyo

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

field = []
top = 12
spot = {'R' : [], 'G' : [], 'B' : [], 'P' : [], 'Y' : []}
for r in range(12):
    data = list(input().rstrip())
    if data.count('.') != 6:
        for c in range(6):
            if data[c] == 'R':
                spot['R'].append((r, c))
            elif data[c] == 'G':
                spot['G'].append((r, c))
            elif data[c] == 'B':
                spot['B'].append((r, c))
            elif data[c] == 'P':
                spot['P'].append((r, c))
            elif data[c] == 'Y':
                spot['Y'].append((r, c))
        if top > r:
            top = r
    field.append(data)
cnt = 0
print(top)
print(field)
print(spot)


