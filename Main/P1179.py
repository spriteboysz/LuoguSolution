#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 09:32:28
LastEditTime: 2021-10-22 09:34:29
Description: 数字统计
FilePath: P1179.py
'''


def func():
    l, r = map(int, input().strip().split())
    count = 0
    for i in range(l, r + 1):
        count += str(i).count("2")
    print(count)


if __name__ == '__main__':
    func()
