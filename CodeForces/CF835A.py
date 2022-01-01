#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 23:34:12
LastEditTime: 2021-11-13 23:36:41
Description: Key races
FilePath: CF835A.py
'''


def func():
    s, v1, v2, t1, t2 = map(int, input().strip().split())
    first = s * v1 + 2 * t1
    second = s * v2 + 2 * t2
    if first > second:
        print("Second")
    elif first < second:
        print("First")
    else:
        print("Friendship")


if __name__ == '__main__':
    func()
