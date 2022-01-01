#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 16:14:20
LastEditTime: 2021-11-28 16:16:34
Description: Flea travel
FilePath: CF55A.py
'''


def func():
    n = int(input())
    if bin(n).count("1") == 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
