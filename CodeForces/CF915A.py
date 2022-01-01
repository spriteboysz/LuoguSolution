#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 16:24:06
LastEditTime: 2021-11-14 16:28:21
Description: Garden
FilePath: CF915A.py
'''


def func():
    _, k = map(int, input().strip().split())
    lst = sorted(map(int, input().strip().split()), reverse=True)
    for item in lst:
        if k % item == 0:
            print(k // item)
            break


if __name__ == '__main__':
    func()
