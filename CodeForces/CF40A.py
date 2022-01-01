#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 21:52:28
LastEditTime: 2021-11-27 22:03:15
Description: Find Color
FilePath: CF40A.py
'''


def func():
    x, y = map(int, input().strip().split())
    radius = (x * x + y * y) ** 0.5
    if radius % 1 == 0:
        print("black")
    elif x * y > 0:
        if int(radius) % 2 == 0:
            print("black")
        else:
            print("white")
    elif x * y < 0:
        if int(radius) % 2 == 0:
            print("white")
        else:
            print("black")



if __name__ == '__main__':
    func()
