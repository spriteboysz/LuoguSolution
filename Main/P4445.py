#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-20 23:55:19
LastEditTime: 2021-12-20 23:57:12
Description: 报名签到
FilePath: P4445.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    distance = 0
    for i in range(0, n - 1):
        distance += max(lst[i], lst[i + 1])
    print(distance)


if __name__ == '__main__':
    func()
