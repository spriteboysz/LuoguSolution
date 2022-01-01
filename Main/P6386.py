#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 00:09:20
LastEditTime: 2021-12-18 15:02:53
Description: VAUVAU 
FilePath: P6386.py
'''


def func():
    a, b, c, d = map(int, input().strip().split())
    p, m, g = map(int, input().strip().split())
    for el in [p, m, g]:
        if 0 < el % (a + b) <= a and 0 < el % (c + d) <= c:
            print("both")
        elif (el % (a + b) == 0 or el % (a + b) > a) and (el % (c + d) == 0 or el % (c + d) > c):
            print("none")
        else:
            print("one")


if __name__ == '__main__':
    func()
