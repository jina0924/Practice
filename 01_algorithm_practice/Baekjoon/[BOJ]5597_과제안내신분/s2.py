# 백준 5597번 과제 안 내신 분..?

import sys
sys.stdin = open('input2.txt')

students = set([i for i in range(1, 31)])
for n in range(28):
    student = int(input())
    students.remove(student)
for bad in list(students):
    print(bad)