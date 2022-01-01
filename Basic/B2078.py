#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:32:37
Description: 含k个3的数
FilePath: B2078.py
'''


def func():
    m, k = map(int, input().strip().split())
    if str(m).count("3") == k:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
