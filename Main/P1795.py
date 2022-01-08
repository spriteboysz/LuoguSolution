#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 21:55:22
LastEditTime: 2022-01-08 22:24:02
Description: 无穷的序列
FilePath: P1795.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = int(((n - 1) * 2) ** 0.5)
        print(1 if a * (a + 1) == (n - 1) * 2 else 0)


if __name__ == '__main__':
    func()
