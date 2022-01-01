#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 22:43:30
LastEditTime: 2021-10-22 22:56:48
Description: 成绩
FilePath: P5082.py
'''


def func():
    n = int(input())
    total, point = 0, 0
    for _ in range(n):
        total += int(input())
    for _ in range(n):
        point += int(input())

    grade = (total * 3 - point * 2) / (total - point)
    print("%.6f" % grade)


if __name__ == '__main__':
    func()
