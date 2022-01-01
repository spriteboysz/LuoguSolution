#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 23:08:57
LastEditTime: 2021-12-23 23:10:29
Description: Couple number
FilePath: P1348.py
'''


def func():
    a, b = map(int, input().strip().split())
    count = 0
    for i in range(a, b + 1):
        if i % 4 == 0 or i % 2 != 0:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
