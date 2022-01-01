#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-27 22:59:36
LastEditTime: 2021-12-27 23:00:59
Description: Kaučuk
FilePath: P7964.py
'''


def func():
    n = int(input())
    t1, t2, t3 = 0, 0, 0
    for _ in range(n):
        s = input().strip().split()
        if s[0] == "section":
            t1 += 1
            t2 = 0
        if s[0] == "subsection":
            t2 += 1
            t3 = 0
        if s[0] == "subsubsection":
            t3 += 1
        if t2 == 0:
            t = str(t1)
        elif t3 == 0:
            t = str(t1) + "." + str(t2)
        else:
            t = str(t1) + "." + str(t2) + "." + str(t3)

        print(t, s[1])


if __name__ == "__main__":
    func()
