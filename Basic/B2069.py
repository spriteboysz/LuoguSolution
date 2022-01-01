#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:13:15
Description: 求分数序列和
FilePath: B2069.py
'''


def func():
    n = int(input())

    p, q, total = 1, 2, 0
    for _ in range(n):
        total += q / p
        p, q = q, q + p

    print("%.4f" % total)


if __name__ == '__main__':
    func()
