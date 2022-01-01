#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 21:59:34
LastEditTime: 2021-10-31 22:07:47
Description: 评等级
FilePath: P5742.py
'''


def func():
    n = int(input())
    students = []
    for _ in range(n):
        num, subject, expand = map(int, input().strip().split())
        comprehensive = 0.7 * subject + 0.3 * expand
        students.append([num, subject, expand, sum(
            [subject, expand]), comprehensive])

    for item in students:
        if item[3] > 140 and item[4] >= 80:
            print("Excellent")
        else:
            print("Not excellent")


if __name__ == '__main__':
    func()
