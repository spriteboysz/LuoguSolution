#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 17:49:21
LastEditTime: 2021-11-14 17:58:02
Description: Love Song
FilePath: CF1539B.py
'''

import string


def func():
    n, m = map(int, input().strip().split())
    s1 = input().strip()
    base = list(string.ascii_lowercase)
    s2 = []
    for item in s1:
        s2.append(base.index(item) + 1)

    for _ in range(m):
        a, b = map(int, input().strip().split())
        print(sum(s2[a - 1: b]))


if __name__ == '__main__':
    func()
