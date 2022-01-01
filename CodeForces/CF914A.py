#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 15:33:01
LastEditTime: 2021-11-14 16:06:01
Description: Perfect Squares
FilePath: CF914A.py
'''


def func():
    n = int(input())
    lst = list(sorted(map(int, input().strip().split()), reverse=True))
    for item in lst:
        if item < 0:
            print(item)
            break
        if int(item ** 0.5) ** 2 != item:
            print(item)
            break


if __name__ == '__main__':
    func()
