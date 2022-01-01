#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:56:19
LastEditTime: 2021-11-04 00:05:01
Description: Towers
FilePath: CF37A.py
'''


def func():
    n = int(input())
    bars = list(map(int, input().strip().split()))
    height = max(map(lambda el: bars.count(el), list(set(bars))))
    total = len(set(bars))
    print(height, total)


if __name__ == '__main__':
    func()
