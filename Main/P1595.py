#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-06 23:34:24
LastEditTime: 2022-01-06 23:36:04
Description: 信封问题
FilePath: P1595.py
'''


def mail(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n - 1) * (mail(n - 2) + mail(n - 1))


def func():
    n = int(input())
    print(mail(n))


if __name__ == '__main__':
    func()
