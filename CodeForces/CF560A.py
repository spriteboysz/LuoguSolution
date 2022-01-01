#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:35:59
LastEditTime: 2021-11-30 23:38:02
Description: Currency System in Geraldion
FilePath: CF560A.py
'''


def func():
    n = int(input())
    banknotes = input().strip().split()
    if "1" in banknotes:
        print(-1)
    else:
        print(1)


if __name__ == '__main__':
    func()
