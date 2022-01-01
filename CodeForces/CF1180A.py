#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:57:01
LastEditTime: 2021-11-20 15:00:01
Description: Alex and a Rhombus
FilePath: CF1180A.py
'''

def func():
    n = int(input())
    count = 1
    for i in range(2, n + 1):
        count += 4 * (i - 1)
    print(count)


if __name__ == '__main__':
    func()
    