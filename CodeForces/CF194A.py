#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 00:04:04
LastEditTime: 2021-11-30 00:06:41
Description: Exams
FilePath: CF194A.py
'''


def func():
    n, k = map(int, input().strip().split())
    print(max(0, 3 * n - k))


if __name__ == '__main__':
    func()
    