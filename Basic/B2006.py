#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 21:40:51
LastEditTime: 2021-09-26 21:44:55
Description: 地球人口承载力估计
FilePath: B2006.py
'''


def func():
    x, a, y, b = map(int, input().strip().split())
    year = (b * y - a * x) / (b - a)
    print("%.2f" % year)


if __name__ == '__main__':
    func()
