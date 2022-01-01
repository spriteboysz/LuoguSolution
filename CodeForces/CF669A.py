#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:03:45
LastEditTime: 2021-12-03 22:07:43
Description: Little Artem and Presents
FilePath: CF669A.py
'''


def func():
    n = int(input())
    if n % 3 == 0:
        print(n // 3 * 2)
    else:
        print(n // 3 * 2 + 1)


if __name__ == '__main__':
    func()
