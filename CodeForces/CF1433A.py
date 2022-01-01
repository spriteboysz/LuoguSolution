#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:27:07
LastEditTime: 2021-11-24 23:35:02
Description: Boring Apartments
FilePath: CF1433A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        num = input().strip()
        print(10 * (int(num[0]) - 1) + (1 + len(num)) * len(num) // 2)


if __name__ == '__main__':
    func()
