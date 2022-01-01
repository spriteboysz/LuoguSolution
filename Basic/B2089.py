#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:08:42
Description: 数组逆序重存放
FilePath: B2089.py
'''


def func():
    n = int(input())
    lst = list(map(str, input().strip().split()))
    print(" ".join(lst[::-1]))


if __name__ == '__main__':
    func()
