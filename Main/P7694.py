#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-28 00:06:19
LastEditTime: 2021-10-28 00:08:19
Description: AUTORI
FilePath: P7694.py
'''


def func():
    names = input().strip().split("-")
    s = ""
    for item in names:
        s += item[0]
    print(s)


if __name__ == '__main__':
    func()
