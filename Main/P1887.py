#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-25 23:26:44
LastEditTime: 2021-10-25 23:36:14
Description: 乘积最大3
FilePath: P1887.py
'''


def func():
    n, m = map(int, input().strip().split())
    div, mod = divmod(n, m)
    lst = [div] * (m - mod) + [div + 1] * mod
    print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
