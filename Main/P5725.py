#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 14:52:35
Description: 求三角形
FilePath: P5725.py
'''


def func():
    n = int(input())
    # 打印正方形
    m = 1
    for i in range(0, n):
        for j in range(0, n):
            print("%02d" % m, end="")
            m += 1
        print()

    # 打印三角形
    print()
    m = 1
    for i in range(0, n):
        for k in range(i + 1, n):
            print(" " * 2, end="")
        for j in range(n - i - 1, n):
            print("%02d" % m, end="")
            m += 1
        print()


if __name__ == '__main__':
    func()
