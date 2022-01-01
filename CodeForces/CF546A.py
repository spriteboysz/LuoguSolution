#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 23:32:07
LastEditTime: 2021-11-20 23:40:03
Description: Soldier and Bananas
FilePath: CF546A.py
'''


def func():
    k, n, w = map(int, input().strip().split())
    total = (k + w * k) * w // 2
    print(total - n if total > n else 0)


if __name__ == '__main__':
    func()
