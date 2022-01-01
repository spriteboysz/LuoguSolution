#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:28:16
Description: 计数问题
FilePath: P1980.py
'''


def func():
    n, x = map(int, input().strip().split())

    count = 0
    for i in range(1, n + 1):
        count += str(i).count(str(x))
    print(count)


if __name__ == '__main__':
    func()
