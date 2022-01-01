#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 23:33:55
LastEditTime: 2021-12-21 23:39:31
Description: 小球
FilePath: P2705.py
'''


def func():
    r, b, c, d, e = map(int, input().strip().split())
    flag = True if r > b else False
    if c + d > e * 2:
        point = r * c + b * d
    else:
        if flag:
            point = b * 2 * e + (r - b) * c
        else:
            point = r * 2 * e + (b - r) * d
    print(point)


if __name__ == '__main__':
    func()
