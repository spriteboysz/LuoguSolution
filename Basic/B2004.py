#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 14:55:01
Description: 对齐输出
FilePath: B2004.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    print("%8d %8d %8d" % (a, b, c))


if __name__ == '__main__':
    func()
