#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-29 00:02:42
LastEditTime: 2021-10-29 00:09:52
Description: 三连击
FilePath: P1008.py
'''


def func():
    s = ""
    for i in range(123, 333):
        s = str(i) + str(2 * i) + str(3 * i)
        if "0" not in s and len(set(s)) == 9:
            print(i, 2 * i, 3 * i)


if __name__ == '__main__':
    func()
    