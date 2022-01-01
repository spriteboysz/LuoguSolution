#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 23:14:56
LastEditTime: 2021-12-15 23:22:18
Description: 饱食
FilePath: P7566.py
'''


def func():
    m, c, o, i = 0, 0, 0, 0
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if s[0] == "M":
            m += 1
        if s[0] == "C":
            c += 1
        if s[0] == "O":
            o += 1
        if s[0] == "I":
            i += 1
    print(m * c * o + m * c * i + m * o * i + c * o * i)


if __name__ == '__main__':
    func()
