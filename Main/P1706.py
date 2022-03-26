#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-02 16:40:02
LastEditTime: 2022-03-25 22:45:46
Description: 全排列问题
FilePath: P1706.py
"""

from itertools import permutations


def func():
    n = int(input())
    for item in permutations(range(1, n + 1)):
        print("%5s" * n % (item))


if __name__ == "__main__":
    func()
