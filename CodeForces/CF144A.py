#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-03 21:42:24
LastEditTime: 2021-12-03 21:56:18
Description: Arrival of the General
FilePath: CF144A.py
'''


def func():
    n = int(input())
    heights = list(map(int, input().strip().split()))
    maxindex = heights.index(max(heights))
    minindex = heights[::-1].index(min(heights))
    count = maxindex + minindex
    if n - 1 - minindex < maxindex:
        count -= 1
    print(count)


if __name__ == '__main__':
    func()
