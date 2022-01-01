#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 15:01:54
LastEditTime: 2021-11-20 15:15:14
Description: Middle of the Contest
FilePath: CF1133A.py
'''


def func():
    hh1, mm1 = map(int, input().strip().split(":"))
    hh2, mm2 = map(int, input().strip().split(":"))
    minutes = (hh2 * 60 + mm2 - hh1 * 60 - mm1) / 2 + hh1 * 60 + mm1
    hh3 = minutes // 60
    mm3 = minutes % 60
    print("%02d:%02d" % (hh3, mm3))


if __name__ == '__main__':
    func()
