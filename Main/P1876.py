#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-25 23:10:31
LastEditTime: 2021-10-25 23:22:13
Description: 开灯
FilePath: P1876.py
'''


def func():
    n = int(input())

    for i in range(1, int(n ** 0.5) + 1):
        print(i * i, end=" ")


if __name__ == '__main__':
    func()
