#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 23:59:51
LastEditTime: 2021-11-21 00:12:04
Description: Jeff and Digits
FilePath: CF352A.py
'''


def func():
    _ = int(input())
    num = input().strip().split()
    if num.count("0") == 0:
        print(-1)
    elif num.count("5") < 9:
        print(0)
    else:
        print("5" * (num.count("5") // 9 * 9) + "0" * num.count("0"))


if __name__ == '__main__':
    func()
