#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:02:47
Description: 计算分数加减表达式的值
FilePath: B2070.py
'''

def func():
    n = int(input())

    total = 0
    for i in range(1, n + 1):
        total += (-1) ** (i - 1) * (1 / i)

    print("%.4f" % total)

if __name__ == '__main__':
    func()
    