#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 22:48:27
LastEditTime: 2021-12-01 23:13:21
Description: Nineteen
FilePath: CF393A.py
'''


def func():
    s = input().strip()
    n, i, e, t = 0, 0, 0, 0
    for w in range(len(s)):
        if s[w] == "n":
            n += 1
        if s[w] == "i":
            i += 1
        if s[w] == "e":
            e += 1
        if s[w] == "t":
            t += 1
    n = max(0, (n - 1) // 2)
    e = e // 3
    print(min(n, i, e, t))


if __name__ == '__main__':
    func()
