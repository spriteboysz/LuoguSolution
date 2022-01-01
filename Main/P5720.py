#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:13:21
Description: 一尺之棰
FilePath: P5720.py
'''

def func():
    a = int(input())

    count = 1
    while a != 1:
        a = a // 2
        count += 1

    print(count)

if __name__ == '__main__':
    func()
    