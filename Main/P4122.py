#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 15:02:17
LastEditTime: 2022-01-01 15:18:50
Description: Blocked Billboard B
FilePath: P4122.py
'''


def func():
    x11, y11, x12, y12 = map(int, input().strip().split())
    x21, y21, x22, y22 = map(int, input().strip().split())
    x31, y31, x32, y32 = map(int, input().strip().split())

    s1 = abs(x11 - x12) * abs(y11 - y12)
    s2 = abs(x21 - x22) * abs(y21 - y22)
    s13 = max(0, min(x12, x32) - max(x11, x31)) * \
        max(0, min(y12, y32) - max(y11, y31))
    s23 = max(0, min(x22, x32) - max(x21, x31)) * \
        max(0, min(y22, y32) - max(y21, y31))
    print(s1 + s2 - s13 - s23)


if __name__ == '__main__':
    func()
