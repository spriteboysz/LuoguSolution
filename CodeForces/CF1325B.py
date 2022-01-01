#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 22:18:22
LastEditTime: 2021-11-13 22:21:19
Description: CopyCopyCopyCopyCopy
FilePath: CF1325B.py
'''


def func():
    n = int(input())
    for _ in range(n):
        _ = int(input())
        lst = set(map(int, input().strip().split()))
        print(len(lst))


if __name__ == '__main__':
    func()
    