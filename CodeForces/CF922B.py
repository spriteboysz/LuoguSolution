#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 22:47:53
LastEditTime: 2021-11-22 22:58:33
Description: Magic Forest
FilePath: CF922B.py
'''


def func():
    n = int(input())
    count = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = a ^ b
            if a + b > c and b <= c <= n:
                count += 1
    print(count)


if __name__ == '__main__':
    func()
