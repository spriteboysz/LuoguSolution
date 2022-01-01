#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 14:41:39
Description: 数字直角三角形
FilePath: P5721.py
'''


def func():
    n = int(input())
    m = 1
    for i in range(0, n):
        for j in range(i, n):
            print("%02d" % m, end="")
            m += 1
        print()


if __name__ == '__main__':
    func()
