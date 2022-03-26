#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-12-04 23:09:16
LastEditTime: 2022-03-25 22:40:38
Description: 组合的输出
FilePath: P1157.py
"""

from itertools import combinations


def func():
    n, r = map(int, input().strip().split())
    for item in combinations(range(1, n + 1), r):
        # print("".join(map(str, item)))
        print("%3s" * r % (item))


if __name__ == "__main__":
    func()
