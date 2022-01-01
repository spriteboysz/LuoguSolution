#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:02:46
LastEditTime: 2021-11-19 23:06:44
Description: Paper Airplanes
FilePath: CF965A.py
'''

from math import ceil

def func():
    k, n, s, p = map(int, input().strip().split())
    print(ceil(ceil(n / s) * k / p))

if __name__ == '__main__':
    func()
    