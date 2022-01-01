#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 14:20:03
LastEditTime: 2021-12-18 14:35:32
Description: NOI
FilePath: P6850.py
'''


def func():
    a, b, c, d, e, f, g, h, i = map(int, input().strip().split())
    score = 50 + a + b + c + d + e + f + g
    if h == 1:
        score += 5
    print("AKIOI" if score >= i else "AFO")


if __name__ == '__main__':
    func()
