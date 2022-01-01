#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 00:04:24
LastEditTime: 2021-11-16 22:59:06
Description: Adjacent Replacements
FilePath: CF1006A.py
'''


def func():
    _ = int(input())
    lst = list(map(int, input().strip().split()))
    lst = list(map(str, map(lambda num: (num - 1) if num % 2 == 0 else num, lst)))
    print(" ".join(lst))


if __name__ == '__main__':
    func()
