#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 22:02:12
LastEditTime: 2021-12-19 22:09:11
Description: 进制转换
FilePath: P2084.py
'''


def func():
    m, num = input().strip().split()
    length = len(num)
    s = ""
    for i, v in enumerate(num):
        if v != "0":
            s += v + "*" + m + "^" + str(length - 1 - i) + "+"
    print(s[:-1])


if __name__ == '__main__':
    func()
