#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 22:17:56
LastEditTime: 2021-12-05 22:24:50
Description: 上学迟到
FilePath: P5707.py
'''


def func():
    s, v = map(int, input().strip().split())
    minitues = s / v + 10
    if minitues <= 8 * 60:
        hh, mm = divmod((60 * 8 - minitues), 60)
    else:
        hh, mm = divmod(60 * (8 + 24) - minitues, 60)
    print("%02d:%02d" % (hh, mm))


if __name__ == '__main__':
    func()
