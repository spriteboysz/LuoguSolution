#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 16:02:40
LastEditTime: 2021-11-28 16:12:06
Description: Square Earth?
FilePath: CF57A.py
'''


def func():
    n, x1, y1, x2, y2 = map(int, input().strip().split())
    if abs(x1 - x2) == n:
        print(n + min(y1 + y2, 2 * n - y1 - y2))
    elif abs(y1 - y2) == n:
        print(n + min(x1 + x2, 2 * n - x1 - x2))
    else:
        print(abs(x1 - x2) + abs(y1 - y2))


if __name__ == '__main__':
    func()
