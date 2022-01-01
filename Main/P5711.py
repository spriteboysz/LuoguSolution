#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-25 21:33:44
LastEditTime: 2021-09-25 21:38:08
Description: 闰年判断
FilePath: P5711.py
'''


def func():
    year = int(input())
    if year % 100 == 0 and year % 400 != 0:
        print(0)
    elif year % 4 == 0:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    func()
