#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 22:55:41
LastEditTime: 2021-11-18 23:59:52
Description: Links and Pearls
FilePath: CF980A.py
'''


def func():
    s = input().strip()
    if s.count("o") == 0 or s.count("-") == 0:
        print("YES")
    elif s.count("-") % s.count("o") == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
