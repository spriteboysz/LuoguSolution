#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 23:38:14
Description: 均值
FilePath: B0255.py
'''

def func():
    num = int(input())
    lst = list(map(float, input().strip().split()))
    print("%.4f" % (sum(lst)/num))


if __name__ == '__main__':
    func()
    