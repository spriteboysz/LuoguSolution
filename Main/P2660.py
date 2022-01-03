#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-03 22:44:07
LastEditTime: 2022-01-03 23:03:09
Description: zzc 种田
FilePath: P2660.py
'''


def func():
    x, y = map(int, input().strip().split())
    strength = 0
    while x != 0 and y != 0:
        if x < y:
            x, y = y, x
        div, mod = divmod(x, y)
        strength += 4 * y * div
        x, y = mod, y

    print(strength)


if __name__ == '__main__':
    func()
