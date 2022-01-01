#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 16:24:38
LastEditTime: 2021-11-21 16:31:47
Description: Vanya and Cubes
FilePath: CF492A.py
'''


def func():
    n = int(input())
    for k in range(1, 100):
        if k * (k + 1) * (k + 2) > 6 * n:
            print(k - 1)
            break


if __name__ == '__main__':
    func()
