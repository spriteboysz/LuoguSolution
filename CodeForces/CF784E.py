#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 15:59:02
LastEditTime: 2021-11-28 16:01:22
Description: Twisted Circuit
FilePath: CF784E.py
'''


def func():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    print(((a ^ b) & (c | d)) ^ ((b & c) | (a ^ d)))


if __name__ == '__main__':
    func()
