#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:19:19
LastEditTime: 2021-11-26 13:22:02
Description: Ezzat and Two Subsequences
FilePath: CF1557A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        maximum = max(lst)
        lst.remove(maximum)
        print("%.8f" % (maximum + sum(lst)/(n - 1)))


if __name__ == '__main__':
    func()
