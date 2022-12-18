# 백준 1092번 배

import sys
sys.stdin = open('input4.txt')

N = int(input())    # N: 크레인 수
crane = sorted(list(map(int, input().split())), reverse=True)     # 크레인의 무게 제한
M = int(input())    # M: 박스 수
box = sorted(list(map(int, input().split())), reverse=True)       # 각 박스의 무게

if crane[0] < box[0]:
    print(-1)
    sys.exit()

cnt = 0
while len(box):
    for c in crane:
        for b in box:
            if c >= b:
                box.remove(b)
                break
    cnt += 1
print(cnt)