#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 16:11:42
LastEditTime: 2021-11-14 16:18:26
Description: Modular Exponentiation
FilePath: CF913A.py
'''


def func():
    n, m = int(input()), int(input())
    if n > 30:
        print(m)
    else:
        print(m % (2 ** n))


if __name__ == '__main__':
    func()
