#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 22:47:32
LastEditTime: 2021-11-29 22:49:55
Description: Black Square
FilePath: CF431A.py
'''


def func():
    a = list(map(int, input().strip().split()))
    s = input().strip()
    count = 0
    for item in s:
        count += a[int(item) - 1]
    print(count)


if __name__ == '__main__':
    func()
