#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-11-06 14:08:23
LastEditTime: 2021-11-06 14:21:45
Description: Compote
FilePath: CF746A.py
"""


def func():
    a, b, c = int(input()), int(input()), int(input())
    print(min(a, b // 2, c // 4) * 7)


if __name__ == "__main__":
    func()
