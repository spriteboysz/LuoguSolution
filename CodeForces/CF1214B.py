#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:00:37
LastEditTime: 2021-11-16 23:05:38
Description: Badges
FilePath: CF1214B.py
'''


def func():
    b, g, n = int(input()), int(input()), int(input())
    count = 0
    for i in range(0, b + 1):
        if 0 <= n - i <= g:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
