#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 00:16:56
LastEditTime: 2021-10-31 10:41:25
Description: 奖学金
FilePath: P1093.py
'''


def func():
    n = int(input())
    students = []
    for i in range(n):
        chinese, math, english = map(int, input().strip().split())
        students.append([i + 1, sum([chinese, math, english]), chinese])

    students = sorted(students, key=lambda el: (
        el[1], el[2], -el[0]), reverse=True)
    for i in range(5):
        print(students[i][0], students[i][1])


if __name__ == '__main__':
    func()
