#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 22:05:48
LastEditTime: 2021-11-27 22:11:40
Description: Cubical Planet
FilePath: CF39D.py
'''


def func():
    x1, y1, z1 = map(int, input().strip().split())
    x2, y2, z2 = map(int, input().strip().split())
    if (x1 ^ x2) + (y1 ^ y2) + (z1 ^ z2) == 3:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    func()
