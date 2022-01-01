#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 21:46:28
LastEditTime: 2021-10-10 22:04:29
Description: 计算阶乘
FilePath: P5739.py
'''


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def func():
    n = int(input())
    print(factorial(n))


if __name__ == '__main__':
    func()
