#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 22:42:22
LastEditTime: 2021-10-23 22:44:27
Description: SIBICE
FilePath: P6320.py
'''


def func():
    n, w, h = map(int, input().strip().split())

    length = (w * w + h * h) ** 0.5
    for _ in range(n):
        if int(input()) <= length:
            print("DA")
        else:
            print("NE")


if __name__ == '__main__':
    func()
