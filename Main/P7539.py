#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-27 22:35:52
LastEditTime: 2021-10-27 22:41:33
Description: NOTE
FilePath: P7539.py
'''


def func():
    scale = list(map(int, input().strip().split()))
    if scale == list(range(1, 9)):
        print("ascending")
    elif scale == list(range(8, 0, -1)):
        print("descending")
    else:
        print("mixed")


if __name__ == '__main__':
    func()
