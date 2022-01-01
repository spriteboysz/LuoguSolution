#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 21:55:22
LastEditTime: 2021-12-18 22:35:02
Description: 无穷的序列
FilePath: P1795.py
'''


def func():
    t = int(input())
    lst = []
    for _ in range(t):
        n = int(input())
        a = int(((n - 1) * 2) ** 0.5)
        if a * (a + 1) == (n - 1) * 2:
            lst.append("1")
        else:
            lst.append("0")
    print("\n".join(lst))


if __name__ == '__main__':
    func()
