#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:54:24
LastEditTime: 2021-11-23 23:57:48
Description: Keanu Reeves
FilePath: CF1189A.py
'''


def func():
    _ = int(input())
    s = input().strip()
    if s.count("0") == s.count("1"):
        print(2)
        print(s[0], s[1:])
    else:
        print(1)
        print(s)


if __name__ == '__main__':
    func()
