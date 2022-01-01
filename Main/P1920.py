#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 23:13:21
LastEditTime: 2021-12-29 23:25:49
Description: 成功密码
FilePath: P1920.py
'''


def func():
    x, n = map(float, input().strip().split())
    n = min(100000, int(n))
    total, k = 0, 1
    for i in range(1, n + 1):
        k *= x
        total += k / i
    print("%.4f" % total)


if __name__ == '__main__':
    func()
