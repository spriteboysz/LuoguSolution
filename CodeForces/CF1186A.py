#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 22:22:52
LastEditTime: 2021-11-19 22:24:38
Description: Vus the Cossack and a Contest
FilePath: CF1186A.py
'''


def func():
    n, m, k = map(int, input().strip().split())
    if n <= m and n <= k:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
    