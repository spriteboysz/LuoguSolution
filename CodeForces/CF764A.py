#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:19:47
LastEditTime: 2021-11-22 23:28:44
Description: Taymyr is calling you
FilePath: CF764A.py
'''


def func():
    n, m, z = map(int, input().strip().split())
    count = 0
    for t in range(max(m, n), z + 1):
        if t % n == 0 and t % m == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
