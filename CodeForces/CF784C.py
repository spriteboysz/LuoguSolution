#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:20:25
LastEditTime: 2021-11-30 23:22:04
Description: INTERCALC
FilePath: CF784C.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print(max(lst) ^ lst[-1])


if __name__ == '__main__':
    func()
