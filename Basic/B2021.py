#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 21:20:27
LastEditTime: 2021-12-10 21:23:26
Description: 输出保留 3 位小数的浮点数
FilePath: B2021.py
'''


def func():
    num = float(input())
    print("%.3f" % (num - 0.000000000000001))


if __name__ == '__main__':
    func()
