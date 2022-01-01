#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:29:15
Description: 数字反转
FilePath: P1307.py
'''

def func():
    n = int(input())
    if n >= 0:
        print(int(str(n)[::-1]))
    else:
        print(0 - int(str(abs(n))[::-1]))

if __name__ == '__main__':
    func()
    