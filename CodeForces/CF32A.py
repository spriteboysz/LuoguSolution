#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:41:04
LastEditTime: 2021-11-05 22:45:34
Description: Reconnaissance
FilePath: CF32A.py
'''


def func():
    n, d = map(int, input().strip().split())
    high = list(sorted(map(int, input().strip().split())))
    count = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if high[j] - high[i] <= d:
                count += 1
            else:
                break
    print(2 * count)


if __name__ == '__main__':
    func()
