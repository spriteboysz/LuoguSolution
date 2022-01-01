#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 22:07:59
LastEditTime: 2021-10-10 22:16:55
Description: 集合求和
FilePath: P2415.py
'''


def func():
    lst = list(map(int, input().strip().split()))
    print(2 ** (len(lst) - 1) * sum(lst))


if __name__ == '__main__':
    func()
