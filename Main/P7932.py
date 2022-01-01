#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 00:05:43
LastEditTime: 2021-12-16 00:12:06
Description: TRI
FilePath: P7932.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    if a + b == c:
        print("%d+%d=%d" % (a, b, c))
    elif a - b == c:
        print("%d-%d=%d" % (a, b, c))
    elif a * b == c:
        print("%d*%d=%d" % (a, b, c))
    elif a // b == c:
        print("%d/%d=%d" % (a, b, c))
    elif a == b + c:
        print("%d=%d+%d" % (a, b, c))
    elif a == b - c:
        print("%d=%d-%d" % (a, b, c))
    elif a == b * c:
        print("%d=%d*%d" % (a, b, c))
    elif a == b // c:
        print("%d=%d/%d" % (a, b, c))
    else:
        print(-1)


if __name__ == '__main__':
    func()
