#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 23:16:51
Description: 求一元二次方程
FilePath: B2053.py
'''


def func():
    a, b, c = map(float, input().strip().split())
    root = b * b - 4 * a * c
    if root < 0:
        print("No answer!")
    elif root == 0:
        print("x1=x2=%.5f" % (-b / (2 * a)))
    else:
        x1 = (-b + root ** 0.5) / (2 * a)
        x2 = (-b - root ** 0.5) / (2 * a)
        if x2 < x1:
            x1, x2 = x2, x1
        print("x1=%.5f;x2=%.5f" % (x1, x2))


if __name__ == '__main__':
    func()
