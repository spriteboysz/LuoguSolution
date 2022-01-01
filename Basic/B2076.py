#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 15:35:40
Description: 球弹跳高度的计算
FilePath: B2076.py
'''


def func():
    high = int(input())

    distance = 0
    for _ in range(0, 10):
        distance += high
        high /= 2
        distance += high

    print(distance-high, high)


if __name__ == '__main__':
    func()
