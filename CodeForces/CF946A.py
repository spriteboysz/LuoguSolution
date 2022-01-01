#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 22:59:56
LastEditTime: 2021-11-09 23:01:23
Description: Partition
FilePath: CF946A.py
'''


def func():
    _ = int(input())
    lst = map(abs, map(int, input().strip().split()))
    print(sum(lst))


if __name__ == '__main__':
    func()
