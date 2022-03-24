#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-24 22:49:37
LastEditTime: 2022-03-24 22:53:49
Description: SPAVANAC
FilePath: P8071.py
"""


def func():
    h1, m1 = map(int, input().strip().split())
    minitue1, day = h1 * 60 + m1, 24 * 60
    minitue2 = (minitue1 - 45 + day) % day
    print(*divmod(minitue2, 60))


if __name__ == "__main__":
    func()
