#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-24 23:48:01
LastEditTime: 2022-03-24 23:51:36
Description: 破译の论
FilePath: P8152.py
"""


def func():
    n, k = map(int, input().strip().split())
    # 1+(n^2-1)×k
    mod = 998244353
    print(((n ** 2 - 1) * k + 1) % mod)


if __name__ == "__main__":
    func()
