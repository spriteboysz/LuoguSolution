#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-07 22:47:03
LastEditTime: 2021-12-07 22:55:33
Description: 蜜蜂路线
FilePath: P2437.py
'''


def func():
    m, n = map(int, input().strip().split())
    a, b = 1, 2
    for _ in range(2, n - m):
        count = a + b
        a, b = b, count
    print(count)


if __name__ == '__main__':
    func()
