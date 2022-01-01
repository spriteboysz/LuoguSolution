#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:57:13
Description: 质因数分解
FilePath: P1075.py
'''

def func():
    n = int(input())

    for i in range(2, n, 1):
        if n % i == 0:
            print(n // i)
            break

if __name__ == '__main__':
    func()
    