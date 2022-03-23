#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-23 23:32:25
LastEditTime: 2022-03-23 23:35:10
Description: RIJEČI
FilePath: P8241.py
"""


def func():
    k = int(input())
    a, b = 0, 1
    for _ in range(1, k):
        a, b = b, a + b
    print(a, b)


if __name__ == "__main__":
    func()