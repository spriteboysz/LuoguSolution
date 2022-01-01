#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:18:42
LastEditTime: 2021-11-05 22:21:22
Description: Petya and Strings
FilePath: CF112A.py
'''


def func():
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    if s1 < s2:
        print(-1)
    elif s1 > s2:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    func()
