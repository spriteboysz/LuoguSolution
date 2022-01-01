#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 00:10:06
LastEditTime: 2021-10-24 00:14:53
Description: PET
FilePath: P6408.py
'''


def func():
    order, score = 0, 0
    for i in range(5):
        cur = sum(map(int, input().strip().split()))
        if cur > score:
            score = cur
            order = i
    print(order + 1, score)


if __name__ == '__main__':
    func()
