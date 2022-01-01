#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 23:26:50
LastEditTime: 2021-12-29 23:47:01
Description: 数楼梯
FilePath: P1255.py
'''


def func():
    n = int(input())
    a, b = 1, 2
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(a)


if __name__ == '__main__':
    func()
