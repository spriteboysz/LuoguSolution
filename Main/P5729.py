#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-08 23:38:20
LastEditTime: 2021-12-08 23:44:09
Description: 工艺品制作
FilePath: P5729.py
'''


def func():
    w, x, h = map(int, input().strip().split())

    cuboid = [[[0] * w for _ in range(x)] for _ in range(h)]
    print(cuboid)

    q = int(int(input()))
    for _ in range(q):
        x1, y1, z1, x2, y2, z2 = map(int, input().strip().split())


if __name__ == '__main__':
    func()
    