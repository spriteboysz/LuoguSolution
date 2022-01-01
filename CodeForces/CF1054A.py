#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 14:39:14
LastEditTime: 2021-11-26 22:02:06
Description: Elevator or Stairs
FilePath: CF1054A.py
'''


def func():
    x, y, z, t1, t2, t3 = map(int, input().strip().split())
    stairs = abs(x - y) * t1
    elevator = (abs(z - x) + abs(x - y)) * t2 + 3 * t3
    print("YES" if elevator <= stairs else "NO")


if __name__ == '__main__':
    func()
