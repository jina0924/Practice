# 백준 2609번 최대공약수와 최소공배수

'''
<유클리드 호제법>
양의 정수 a, b가 있고 a를 b로 나눈 나머지를 r이라고 하자.
a와 b의 최대공약수를 (a, b)라고 하면, 다음이 성립된다.
(a, b) = (b, r)
ex) (24, 18) = (18, 6) = (6, 0) = 6

a와 b의 최대공약수를 G, 최소공배수를 L이라 하면
a, b = GA, GB
L = GAB
로 표현 가능
'''

import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
if b > a:
    a, b = b, a
G, q, r = b, a, 1
while True:
    r = q % G
    if r == 0:
        break
    q = G
    G = r
print(G)
print(a * b // G)