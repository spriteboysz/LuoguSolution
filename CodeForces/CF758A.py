#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 23:52:05
LastEditTime: 2021-11-07 23:56:45
Description: Holiday Of Equality
FilePath: CF758A.py
'''


def func():
    _ = int(input())
    welfare = list(map(int, input().strip().split()))
    count, maximum = 0, max(welfare)
    for item in welfare:
        count += maximum - item
    print(count)


if __name__ == '__main__':
    func()
