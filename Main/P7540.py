#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-27 23:00:19
LastEditTime: 2021-10-27 23:02:28
Description: DOMINO
FilePath: P7540.py
'''


def func():
    n = int(input())
    total = 0
    for y in range(0, n + 1):
        for x in range(0, y + 1):
            total = total + x + y
    print(total)


if __name__ == '__main__':
    func()
