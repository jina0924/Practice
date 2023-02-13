# 백준 1620번 나는야 포켓몬 마스터 이다솜

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())        # N: 도감에 수록되어 있는 포켓몬 수, M: 내가 맞춰야하는 문제 수
pokedex_num = {}                        # key가 포켓몬 번호
pokedex_name = {}                       # key가 포켓몬 이름
for i in range(1, N+1):
    pokemon = input().rstrip()
    pokedex_num[i] = pokemon
    pokedex_name[pokemon] = i
for _ in range(M):
    q = input().rstrip()
    if q.isdigit():                     # isdigit(): 문자열이 숫자로만 이루어져 있는지 확인하는 함수
        print(pokedex_num.get(int(q)))
    else:
        print(pokedex_name.get(q))
