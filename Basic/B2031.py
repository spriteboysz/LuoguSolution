#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 22:25:37
LastEditTime: 2021-09-26 22:32:21
Description: 计算三角形面积
FilePath: B2031.py
'''


def distance(x1, y1, x2, y2):
    return (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def func():
    x1, y1, x2, y2, x3, y3 = map(int, input().strip().split())
    a = distance(x1, y1, x2, y2)
    b = distance(x1, y1, x3, y3)
    c = distance(x2, y2, x3, y3)

    p = (a + b + c) * 0.5
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("%.2f" % s)


if __name__ == '__main__':
    func()
