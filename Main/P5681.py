#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 23:13:02
LastEditTime: 2021-10-22 23:15:24
Description: 面积
FilePath: P5681.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    if a * a > b * c:
        return "Alice"
    else:
        return "Bob"


if __name__ == '__main__':
    s = func()
    print(s)
