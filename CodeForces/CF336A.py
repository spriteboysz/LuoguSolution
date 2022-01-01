#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 23:29:53
LastEditTime: 2021-12-01 23:49:13
Description: Vasily the Bear and Triangle
FilePath: CF336A.py
'''


def func():
    a, b = map(int, input().strip().split())
    # y = a * x + b
    if a > 0 and b > 0:
        print("0 %d %d 0" % (a + b, a + b))
    elif a < 0 and b > 0:
        print("%d 0 0 %d" % (a - b, -a + b))
    elif a < 0 and b < 0:
        print("%d 0 0 %d" % (a + b, a + b))
    elif a > 0 and b < 0:
        print("0 %d %d 0" % (-a + b, a - b))


if __name__ == '__main__':
    func()
