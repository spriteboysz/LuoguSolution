#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 14:49:16
Description: 不定方程求解
FilePath: B2086.py
'''


def func():
    a, b, c = map(int, input().strip().split())

    count = 0
    for x in range(0, c + 1):
        for y in range(0, c + 1):
            if a * x + b * y == c:
                count += 1
    print(count)


if __name__ == '__main__':
    func()
