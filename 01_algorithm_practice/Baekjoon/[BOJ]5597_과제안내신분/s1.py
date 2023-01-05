# 백준 5597번 과제 안 내신 분..?

import sys
sys.stdin = open('input2.txt')

students = [0] * 31
for i in range(28):
    student = int(input())
    students[student] = 1
for j in range(1, 31):
    if not students[j]:
        print(j)
