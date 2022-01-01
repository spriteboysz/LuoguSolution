#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 00:00:54
LastEditTime: 2021-12-03 23:15:54
Description: Generate Login
FilePath: CF909A.py
'''


def func():
    a, b = input().strip().split()
    print(a[0], end="")
    for i in range(1, len(a)):
        if a[i] < b[0]:
            print(a[i], end="")
        else:
            break
    print(b[0])


if __name__ == '__main__':
    func()
