#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 15:57:45
LastEditTime: 2021-12-05 15:59:53
Description: 洛谷团队系统
FilePath: P5713.py
'''


def func():
    n = int(input())
    local = n * 5
    luogu = 11 + n * 3
    print("Local" if local < luogu else "Luogu")


if __name__ == '__main__':
    func()
    