#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 23:12:26
LastEditTime: 2021-11-05 23:14:21
Description: George and Accommodation
FilePath: CF467A.py
'''


def func():
    n = int(input())
    count = 0
    for _ in range(n):
        p, q = map(int, input().strip().split())
        if q - p >= 2:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
