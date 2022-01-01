#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:34:00
LastEditTime: 2021-11-11 23:40:33
Description: Ehab and another construction problem
FilePath: CF1088A.py
'''


def func():
    x = int(input())
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            if a * b > x and a / b < x and a % b == 0:
                print(a, b)
                return
    else:
        print(-1)


if __name__ == '__main__':
    func()
