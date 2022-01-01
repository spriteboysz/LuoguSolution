#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-13 22:54:42
LastEditTime: 2021-12-13 22:56:40
Description: 光图
FilePath: P6159.py
'''


def func():
    n, p, k = map(int, input().strip().split())
    print(((p % n) * (k % n)) % n)


if __name__ == '__main__':
    func()
