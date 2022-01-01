#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:36:03
LastEditTime: 2021-11-18 23:42:27
Description: USB Flash Drives
FilePath: CF609A.py
'''


def func():
    n, m = int(input()), int(input())
    capacities = []
    for _ in range(n):
        capacities.append(int(input()))

    size = 0
    for index, item in enumerate(sorted(capacities, reverse=True)):
        size += item
        if size >= m:
            break
    print(index + 1)


if __name__ == '__main__':
    func()
