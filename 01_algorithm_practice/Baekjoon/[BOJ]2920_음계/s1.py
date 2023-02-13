# 백준 2920번 음계

import sys
sys.stdin = open('input3.txt')

scales = list(map(int, input().split()))
scale = scales[0]
if scale == 1:
    ans = 'ascending'
    idx = 1
    while idx < 8:
        if scales[idx] != scale + 1:
            ans = 'mixed'
            break
        scale = scales[idx]
        idx += 1
elif scale == 8:
    ans = 'descending'
    idx = 1
    while idx < 8:
        if scales[idx] != scale - 1:
            ans = 'mixed'
            break
        scale = scales[idx]
        idx += 1
else:
    ans = 'mixed'
print(ans)