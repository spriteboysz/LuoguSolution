#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 23:35:33
LastEditTime: 2021-12-16 23:36:45
Description: SKOCIMIS
FilePath: P6426.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    print(max(abs(a - b), abs(b - c)) - 1)


if __name__ == '__main__':
    func()
