#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 23:39:50
Description: 救援
FilePath: B2066.py
'''

import math


def func():
    n = int(input())

    time = 0
    for _ in range(n):
        x, y, person = map(float, input().strip().split())
        time += (x * x + y * y) ** 0.5 * 2 / 50
        time += person * 1 + person * 0.5

    print(math.ceil(time))


if __name__ == '__main__':
    func()
