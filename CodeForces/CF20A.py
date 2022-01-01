#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 23:15:35
LastEditTime: 2021-11-05 23:19:21
Description: BerOS file system
FilePath: CF20A.py
'''


def func():
    path = input().strip()
    while "//" in path:
        path = path.replace("//", "/")

    if path.endswith("/") and len(path) != 1:
        path = path[:-1]
    print(path)


if __name__ == '__main__':
    func()
