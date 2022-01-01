#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 23:09:09
LastEditTime: 2021-10-30 23:27:46
Description: 谁拿了最多奖学金
FilePath: P1051.py
'''


def func():
    n = int(input())
    students = []
    for _ in range(n):
        scholarship = [0] * 5
        name, *point = input().strip().split()
        if int(point[0]) > 80 and int(point[4]) >= 1:
            scholarship[0] = 8000
        if int(point[0]) > 85 and int(point[1]) > 80:
            scholarship[1] = 4000
        if int(point[0]) > 90:
            scholarship[2] = 2000
        if int(point[0]) > 85 and point[3] == "Y":
            scholarship[3] = 1000
        if int(point[1]) > 80 and point[2] == "Y":
            scholarship[4] = 850
        students.append([name, sum(scholarship)])

    student = max(students, key=lambda el: el[1])
    print(student[0])
    print(student[1])
    total = 0
    for item in students:
        total += item[1]
    print(total)


if __name__ == '__main__':
    func()
