#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 23:57:09
Description: 人口增长问题
FilePath: B2063.py
'''


def func():
    x, n = map(int, input().strip().split())
    for _ in range(n):
        x += x * 0.1 / 100

    print("%.4f" % x)


if __name__ == '__main__':
    func()
