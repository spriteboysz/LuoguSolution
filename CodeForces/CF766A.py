#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:17:33
LastEditTime: 2021-11-22 23:18:54
Description: Mahmoud and Longest Uncommon Subsequence
FilePath: CF766A.py
'''


def func():
    a, b = input().strip(), input().strip()
    if a == b:
        print(-1)
    else:
        print(max(len(a), len(b)))


if __name__ == '__main__':
    func()
