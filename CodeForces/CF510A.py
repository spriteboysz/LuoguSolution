#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 22:58:59
LastEditTime: 2021-11-07 23:01:43
Description: Fox And Snake
FilePath: CF510A.py
'''


def func():
    n, m = map(int, input().strip().split())
    for i in range(n):
        if i % 2 == 0:
            print("#" * m)
        elif i % 4 == 1:
            print("." * (m - 1) + "#")
        else:
            print("#" + "." * (m - 1))


if __name__ == '__main__':
    func()
