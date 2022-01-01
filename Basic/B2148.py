#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 22:21:23
Description: 再求f(x,n)
FilePath: B2148.py
'''


def func():
    x, n = map(float, input().strip().split())
    total = x
    for i in range(1, int(n) + 1):
        total = x / (i + total)
            
    print("%.2f" % total)


if __name__ == '__main__':
    func()
