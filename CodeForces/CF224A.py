#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:14:03
LastEditTime: 2021-11-02 23:23:25
Description: Parallelepiped
FilePath: CF224A.py
'''


def func():
    areas = list(map(int, input().strip().split()))
    a = (areas[0] * areas[1] / areas[2]) ** 0.5
    b = areas[0] / a
    c = areas[1] / a
    return 4 * int(a + b + c)


if __name__ == '__main__':
    ans = func()
    print(ans)
