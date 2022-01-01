#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 15:28:33
Description: 幂的末尾
FilePath: B2075.py
'''

def func():
    a, b = map(int, input().strip().split())

    power = 1
    for _ in range(b):
        power = (power * a) % 1000

    print("%03d" % power)

if __name__ == '__main__':
    func()
    