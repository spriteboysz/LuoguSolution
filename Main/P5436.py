#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 22:07:22
LastEditTime: 2021-12-29 22:11:26
Description: 缘分
FilePath: P5436.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("1" if n == 1 else (n * (n - 1)))


if __name__ == '__main__':
    func()
