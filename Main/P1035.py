#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:35:09
Description: 级数求和
FilePath: P1035.py
'''

def func():
    k = int(input())

    n, s = 1, 0
    while s <= k:
        s += 1 / n
        n += 1

    print(n - 1)
        

if __name__ == '__main__':
    func()
    