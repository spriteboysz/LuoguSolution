#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 21:48:12
LastEditTime: 2021-12-01 21:53:33
Description: Friends Meeting
FilePath: CF931A.py
'''


def func():
    a, b = int(input()), int(input())
    dis1 = abs(a - b) // 2
    dis2 = abs(a - b) - dis1
    print((1 + dis1) * dis1 // 2 + (1 + dis2) * dis2 // 2)


if __name__ == '__main__':
    func()
