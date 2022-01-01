#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:36:22
Description: 计算多项式的值
FilePath: B2080.py
'''

def func():
    x, n = input().strip().split()
    x, n = float(x), int(n)
    
    value = 0
    for i in range(0, n + 1):
        value += x ** i

    print("%.2f" % value)


if __name__ == '__main__':
    func()
    
