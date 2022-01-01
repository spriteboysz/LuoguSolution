#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 23:11:48
LastEditTime: 2021-12-23 23:21:09
Description: 连续自然数和
FilePath: P1147.py
'''


def func():
    m = int(input())
    for i in range(1, m // 2 + 1):
        total = 0
        for j in range(i, m + 1):
            total += j
            if total >= m:
                break
        if total == m:
            print(i, j)


if __name__ == '__main__':
    func()
