#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 23:53:37
LastEditTime: 2021-11-30 00:01:41
Description: Problem About Equation
FilePath: CF174A.py
'''


def func():
    n, b = map(int, input().strip().split())
    cpu = list(map(int, input().strip().split()))
    avenge = (sum(cpu) + b) / n
    if avenge < max(cpu):
        print(-1)
    else:
        for item in [(avenge - i) for i in cpu]:
            print("%.6f" % item)


if __name__ == '__main__':
    func()
